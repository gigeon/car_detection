from PySide2.QtCore import QThread, Signal
from PySide2.QtGui import QPixmap, QImage
import cv2
import time


class ShowVideoThread(QThread):
    change_pixmap_signal = Signal(QImage, name="showVideoSignal")

    def __init__(self, path):
        super().__init__()
        self.path = path
        self._run_flag = True

    def run(self):
        cap = cv2.VideoCapture(self.path)
        while self._run_flag and cap.isOpened():
            ret, cv_img = cap.read()
            if ret:
                rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.change_pixmap_signal.emit(qt_image)
                time.sleep(0.05)
            else:
                break
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()