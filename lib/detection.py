import torch
import cv2
from PySide2.QtCore import QThread, Signal
from PySide2.QtGui import QPixmap, QImage
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'
import re


class detectionClass(QThread):
    detection_signal = Signal(list, name="detectionSignal")
    change_pixmap_signal = Signal(QImage, name="showVideoSignal")
    
    def __init__(self, file, flag):
        super().__init__()
        self.model_yolo = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        self.model_east = "frozen_east_text_detection.pb"
        self.img_list = []
        self.plt_list = []
        self.num_list = []
        self.file = file
        self.flag = flag
        
    def run(self):
        if self.flag == 1:
            self.detection_video(self.file)
        if self.flag == 0:
            self.detection_image(self.file)
        
        self.detection_plate()
        self.detection_number()
        self.detection_signal.emit(self.num_list)
        
    def detection_video(self, path):
        cap = cv2.VideoCapture(path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            results = self.model_yolo(frame)
            objects = results.xyxy[0][(results.xyxy[0][:, 5] == 7) & (results.xyxy[0][:, 4] >= 0.5)]

            for obj in objects:
                xmin, ymin, xmax, ymax, confidence, class_id = obj[:6]
                print(f'Class: {int(class_id)}, Confidence: {confidence:.2f}, Bounding Box: ({xmin:.2f}, {ymin:.2f}) - ({xmax:.2f}, {ymax:.2f})')
                self.img_list.append(frame[int(ymin):int(ymax), int(xmin):int(xmax)])
            
        cap.release()
            
    def detection_image(self, img):
        results = self.model_yolo(img)
        objects = results.xyxy[0][(results.xyxy[0][:, 5] == 7) & (results.xyxy[0][:, 4] >= 0.7)]
        for obj in objects:
            xmin, ymin, xmax, ymax, confidence, class_id = obj[:6]
            print(f'Class: {int(class_id)}, Confidence: {confidence:.2f}, Bounding Box: ({xmin:.2f}, {ymin:.2f}) - ({xmax:.2f}, {ymax:.2f})')
            self.img_list.append(img[int(ymin):int(ymax), int(xmin):int(xmax)])
    
    def detection_plate(self):
        try:
            net = cv2.dnn.readNet(self.model_east)
            for img in self.img_list:
                orig = img.copy()
                (H, W) = img.shape[:2]
                newW, newH = (320, 320)
                rW = W / float(newW)
                rH = H / float(newH)
                img = cv2.resize(img, (newW, newH))
                blob = cv2.dnn.blobFromImage(img, 1.0, (newW, newH), (123.68, 116.78, 103.94), swapRB=True, crop=False)
                
                net.setInput(blob)
                (scores, geometry) = net.forward(["feature_fusion/Conv_7/Sigmoid", "feature_fusion/concat_3"])

                rects, confidences = self.decode_predictions(scores, geometry, 0.5)

                indices = cv2.dnn.NMSBoxes(rects, confidences, 0.5, 0.4)

                if len(indices) > 0:
                    for i, idx in enumerate(indices.flatten()):
                        (startX, startY, endX, endY) = rects[idx]
                        startX = int(startX * rW)
                        startY = int(startY * rH)
                        endX = int(endX * rW)
                        endY = int(endY * rH)
                        
                        # 검출된 영역 자르기
                        cropped = orig[startY:endY, startX-20:endX+20]
                        self.plt_list.append(cropped)
        except:
            pass
    
    def detection_number(self):
        try:
            for plt in self.plt_list:
                scale_factor = 4  # 확대할 배율
                height, width = plt.shape[:2]
                new_height, new_width = height * scale_factor, width * scale_factor
                resized_image = cv2.resize(plt, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

                gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
                config='--psm 7 --oem 0'
                text = pytesseract.image_to_string(gray, lang='kor', config=config)
                text = re.sub('[^가-힣0-9]', '', text)
                print(text)
                self.num_list.append(text)
        except:
            pass
    
    def decode_predictions(self, scores, geometry, scoreThresh):
        numRows, numCols = scores.shape[2:4]
        rects = []
        confidences = []

        for y in range(numRows):
            scoresData = scores[0, 0, y]
            xData0 = geometry[0, 0, y]
            xData1 = geometry[0, 1, y]
            xData2 = geometry[0, 2, y]
            xData3 = geometry[0, 3, y]
            anglesData = geometry[0, 4, y]

            for x in range(numCols):
                if scoresData[x] < scoreThresh:
                    continue

                (offsetX, offsetY) = (x * 4.0, y * 4.0)
                angle = anglesData[x]
                cos = np.cos(angle)
                sin = np.sin(angle)

                h = xData0[x] + xData2[x]
                w = xData1[x] + xData3[x]

                endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
                endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
                startX = int(endX - w)
                startY = int(endY - h)

                rects.append((startX, startY, endX, endY))
                confidences.append(float(scoresData[x]))

        return rects, confidences