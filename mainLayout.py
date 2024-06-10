from PySide2.QtCore import Slot
from PySide2.QtWidgets import QFileDialog
from PySide2.QtGui import QPixmap, QImage
import cv2
import os
from datetime import datetime
import np
from lib.detection import detectionClass
from lib.layoutClass import layoutClass
from lib.VideoThread import ShowVideoThread
from sendLayout import sendLayoutClass
from ui.ui_main import Ui_Main


class mainLayoutClass(layoutClass, Ui_Main) :
    def __init__(self, app, dbc):
        super(mainLayoutClass, self).__init__()
        self.setupUi(self)
        self.set_logo()
        self.app = app
        self.dbc = dbc
        self.file_btn.clicked.connect(self.file_upload)
        self.send_btn.clicked.connect(self.show_send)
        self.hide_btn.clicked.connect(lambda: self.hide_btn.setVisible(False))
        self.ok_btn.clicked.connect(self.show_setting)
        self.file = None
        self.path = None
        self.video_thread = None
        self.detection_thread = None
        
        query = "SELECT SPOT_NAME FROM CONFIG"
        rows = dbc.select(query)
        self.spot_lbl.setText(rows[0]["spot_name"])
        
        self.show_num_list()
    
    
    def file_upload(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.path, _ = QFileDialog.getOpenFileName(self, "Select an Image", "", \
            "All Files (*);;Image Files (*.png;*.jpg;*.jpeg);;Video Files (*.mp4;*.avi;*.mov)", options=options)
        if self.path:
            self.path = os.path.normpath(self.path)
            self.get_file()
    
    def get_file(self):
        
        if self.path.lower().endswith(('.png', '.jpg', '.jpeg')):
            self.file = cv2.imdecode(np.fromfile(self.path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            self.show_img_label(self.file)
            flag = 0
                
        elif self.path.lower().endswith(('.mp4', '.avi', '.mov')):
            self.file = cv2.VideoCapture(self.path)
            self.video_thread = ShowVideoThread(self.path)
            self.video_thread.change_pixmap_signal.connect(self.show_vid_label)
            self.video_thread.start()
            flag = 1
        
        if self.file is not None:
            self.detection_thread = detectionClass(self.file, flag)
            self.detection_thread.detection_signal.connect(self.insert_data)
            self.detection_thread.start()
        
        
                
    def show_img_label(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img_rgb.shape
        bytes_per_line = ch * w
        qimg = QImage(img_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)
        
        self.vid_lbl.setPixmap(pixmap)
        self.vid_lbl.setScaledContents(True)
            
    @Slot(QImage, name="showVideoSignal")
    def show_vid_label(self, qt_image):
        self.vid_lbl.setPixmap(QPixmap.fromImage(qt_image))
        self.vid_lbl.setScaledContents(True)
    
    # def closeEvent(self, event):
    #     if self.video_thread is not None:
    #         self.video_thread.stop()
    #     event.accept()
    
    @Slot(list, name="detectionSignal")
    def insert_data(self, nums):
        now = datetime.now().strftime('%Y-%m-%d')
        for num in nums:
            query = f"INSERT INTO NUMBER(CAR_NO, DATE) VALUES('{num}', '{now}')"
            self.dbc.insert(query)
            self.show_num_list()
    
    def show_num_list(self):
        query = "SELECT ID, CAR_NO FROM NUMBER"
        rows = self.dbc.select(query)
        for row in rows:
            self.number_list.append(row['car_no'])
    
    def show_send(self):
        self.sendLayout = sendLayoutClass(self.dbc)
        dlg_rect = self.sendLayout.frameGeometry()
        center_pointer = self.mapToGlobal(self.rect().center())
        dlg_rect.moveCenter(center_pointer)
        self.sendLayout.move(dlg_rect.topLeft())
        self.sendLayout.show()
        
    def show_setting(self):
        ...