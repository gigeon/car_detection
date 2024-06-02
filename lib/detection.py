import torch
import cv2
from PySide2.QtCore import QThread 

class detectionClass():
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        self.imgs = []
        
    def detection_video(self, cap):
        
        output_path = 'test.mp4'
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            results = self.model(frame)
            objects = results.xyxy[0][(results.xyxy[0][:, 5] == 7) & (results.xyxy[0][:, 4] >= 0.3)]

            for obj in objects:
                cv2.imwrite('test.png', obj)
                xmin, ymin, xmax, ymax, confidence, class_id = obj[:6]
                cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
                cv2.putText(frame, f'Truck {confidence:.2f}', (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                print(f'Class: {int(class_id)}, Confidence: {confidence:.2f}, Bounding Box: ({xmin:.2f}, {ymin:.2f}) - ({xmax:.2f}, {ymax:.2f})')

            out.write(frame)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        cap.release()
        out.release()
        cv2.destroyAllWindows()

            
    def dectection_image(self, img):
        results = self.model(img)
        objects = results.xyxy[0][(results.xyxy[0][:, 5] == 7) & (results.xyxy[0][:, 4] >= 0.7)]
        for obj in objects:
            for obj in objects:
                xmin, ymin, xmax, ymax, confidence, class_id = obj[:6]
                print(f'Class: {int(class_id)}, Confidence: {confidence:.2f}, Bounding Box: ({xmin:.2f}, {ymin:.2f}) - ({xmax:.2f}, {ymax:.2f})')
                
    def dectin_number(self):
        ...

