import torch
import cv2
from PySide2.QtCore import QThread, Signal


class detectionClass(QThread):
    detection_signal = Signal(list, name="detectionSignal")
    
    def __init__(self, file, flag):
        super().__init__()
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        self.img_list = []
        self.num_list = []
        self.file = file
        self.flag = flag
        
    def run(self):
        if self.flag == 1:
            self.detection_video(self.file)
        if self.flag == 0:
            self.detection_image(self.file)
        
        self.detection_number()
        print('3')
        self.detection_signal.emit(self.num_list)
        
    def detection_video(self, cap):
        
        # output_path = 'test.mp4'
        # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        # fps = cap.get(cv2.CAP_PROP_FPS)
        # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            results = self.model(frame)
            objects = results.xyxy[0][(results.xyxy[0][:, 5] == 7) & (results.xyxy[0][:, 4] >= 0.3)]

            for obj in objects:
                xmin, ymin, xmax, ymax, confidence, class_id = obj[:6]
                # cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
                # cv2.putText(frame, f'Truck {confidence:.2f}', (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                print(f'Class: {int(class_id)}, Confidence: {confidence:.2f}, Bounding Box: ({xmin:.2f}, {ymin:.2f}) - ({xmax:.2f}, {ymax:.2f})')
                self.img_list.append(frame[int(ymin):int(ymax), int(xmin):int(xmax)])
                print(self.img_list)
            
        cap.release()
            
    def detection_image(self, img):
        results = self.model(img)
        objects = results.xyxy[0][(results.xyxy[0][:, 5] == 7) & (results.xyxy[0][:, 4] >= 0.7)]
        for obj in objects:
            xmin, ymin, xmax, ymax, confidence, class_id = obj[:6]
            print(f'Class: {int(class_id)}, Confidence: {confidence:.2f}, Bounding Box: ({xmin:.2f}, {ymin:.2f}) - ({xmax:.2f}, {ymax:.2f})')
            self.img_list.append(img[int(ymin):int(ymax), int(xmin):int(xmax)])
    
    def detection_number(self):
        for i, img in enumerate(self.img_list):
            cv2.imshow('img', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
