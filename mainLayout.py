from lib.layoutClass import layoutClass
from PySide2.QtCore import (
    Slot,
    Qt,
)
from PySide2.QtWidgets import QFileDialog
from PySide2.QtGui import QPixmap
from ui.ui_main import Ui_Main
import cv2
import os
import np
from lib.detection import detectionClass


class mainLayoutClass(layoutClass, Ui_Main) :
    def __init__(self, app, dbc):
        super(mainLayoutClass, self).__init__()
        self.setupUi(self)
        self.app = app
        self.dbc = dbc
        self.set_logo()
        self.file_btn.clicked.connect(self.file_upload)
        self.file = None
        self.path = None
        
        query = "SELECT SPOT_NAME FROM CONFIG"
        rows = dbc.select(query)
        self.spot_lbl.setText(rows[0]["spot_name"])
        
        query = "SELECT ID, CAR_NO FROM NUMBER"
        rows = dbc.select(query)
        for row in rows:
            self.number_list.append(row['car_no'])
    
    
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
            if self.file is not None:
                detectionClass().dectection_image(self.file)
                
        elif self.path.lower().endswith(('.mp4', '.avi', '.mov')):
            self.file = cv2.VideoCapture(self.path)
            if self.file is not None:
                detectionClass().detection_video(self.file)
            
            
    