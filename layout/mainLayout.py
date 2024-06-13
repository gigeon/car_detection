from PySide2.QtCore import Slot
from PySide2.QtWidgets import QFileDialog
from PySide2.QtGui import QPixmap, QImage
import cv2
import os
import re
import np
from datetime import datetime
from lib.detection import detectionClass
from lib.layoutClass import layoutClass
from lib.VideoThread import ShowVideoThread
from layout.sendLayout import sendLayoutClass
from layout.settingLayout import settingLayoutClass
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
            if self.path is not None:
                self.detection_thread = detectionClass(self.path, flag, self.dbc)
                self.detection_thread.detection_signal.connect(self.insert_data)
                self.detection_thread.start()
                
        elif self.path.lower().endswith(('.mp4', '.avi', '.mov')):
            self.video_thread = ShowVideoThread(self.path)
            self.video_thread.change_pixmap_signal.connect(self.show_vid_label)
            self.video_thread.change_done_signal.connect(self.done_change)
            self.video_thread.start()
            flag = 1
                
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
    
    @Slot(name="doneVideoSignal")
    def done_change(self):
        flag = 1
        self.detection_thread = detectionClass(self.path, flag, self.dbc)
        self.detection_thread.detection_signal.connect(self.insert_data)
        self.detection_thread.start()
    
    @Slot(list, name="detectionSignal")
    def insert_data(self, nums):
        repit_list = []
        now = datetime.now().strftime('%Y-%m-%d')
        for num in nums:
            if re.match(r'^\d{4}$', num) and num not in repit_list:
                repit_list.append(num)
                query = f'INSERT INTO NUMBER(CAR_NO, DATE) VALUES("{num}", "{now}")'
                self.dbc.insert(query)
                self.show_num_list()
    
    def show_num_list(self):
        self.number_list.clear()
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
        query = 'SELECT ADMIN_PWD FROM SETTING'
        rows = self.dbc.select(query)
        if self.pwd_lbl.text() == rows[0]['admin_pwd']:
            self.settingLayout = settingLayoutClass(self.dbc)
            self.settingLayout.setting_close_signal.connect(self.close_signal)
            dlg_rect = self.settingLayout.frameGeometry()
            center_pointer = self.mapToGlobal(self.rect().center())
            dlg_rect.moveCenter(center_pointer)
            self.settingLayout.move(dlg_rect.topLeft())
            self.settingLayout.show()
            
    @Slot(name="closeSettingSignal")
    def close_signal(self):
        self.hide_btn.setVisible(True)
        self.pwd_lbl.setText('')