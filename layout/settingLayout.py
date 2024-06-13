from ui.ui_setting import Ui_Setting
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Signal


class settingLayoutClass(QDialog, Ui_Setting):
    setting_close_signal = Signal(name = "closeSettingSignal")
    
    def __init__(self, dbc):
        super(settingLayoutClass, self).__init__()
        self.dbc = dbc
        self.setupUi(self)
        self.set_logo()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.logo_btn.clicked.connect(self.close_setting)
        self.btn.clicked.connect(self.save_data)
        self.btn_2.clicked.connect(self.save_data)
        self.show_data()
        
        
    def set_logo(self):
        pixmap = QPixmap('images/tino.png')
        pixmap = pixmap.scaled(self.logo_btn.size(),Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon = QIcon(pixmap)
        self.logo_btn.setIcon(icon)
        self.logo_btn.setIconSize(pixmap.size())
        
    def show_data(self):
        conf_query = 'SELECT * FROM CONFIG'
        set_query = 'SELECT * FROM SETTING'
        conf_list = self.dbc.select(conf_query)[0]
        set_list = self.dbc.select(set_query)[0]
        
        self.spot_id.setText(str(conf_list['spot_id']))
        self.spot_name.setText(str(conf_list['spot_name']))
        self.user_id.setText(str(conf_list['user_id']))
        self.user_pwd.setText(str(conf_list['user_pwd']))
        self.api_path.setText(str(set_list['api_path']))
        self.save_path.setText(str(set_list['save_path']))
    
    def save_data(self, event):
        spot_id = self.spot_id.text()
        spot_name = self.spot_name.text()
        user_id = self.user_id.text()
        user_pwd = self.user_pwd.text()
        api_path = self.api_path.text()
        save_path = self.save_path.text()
        
        conf_query = f'UPDATE CONFIG SET \
            SPOT_ID = "{spot_id}", \
            SPOT_NAME = "{spot_name}", \
            USER_ID = "{user_id}", \
            USER_PWD = "{user_pwd}"'
        set_query = f'UPDATE SETTING SET \
            API_PATH = "{api_path}", \
            SAVE_PATH = "{save_path}"'
        self.dbc.update(conf_query)
        self.dbc.update(set_query)
        self.close_setting
    
    def close_setting(self):
        self.close()
        self.setting_close_signal.emit()