from PySide2.QtCore import QThread, Signal
from PySide2.QtGui import QPixmap, QImage
import cv2
import time


class ShowVideoThread(QThread):
    change_pixmap_signal = Signal(QImage, name="showVideoSignal")
    change_done_signal = Signal(name="doneVideoSignal")

    def __init__(self, file):
        super().__init__()
        self.file = file
        self._run_flag = True

    def run(self):
        cap = cv2.VideoCapture(self.file)
        while cap.isOpened():
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
        self.change_done_signal.emit()
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()