from ui.ui_send import Ui_Send
from lib.layoutClass import layoutClass
from lib.makeExcel import makeExcelClass
import requests
import json

class sendLayoutClass(layoutClass, Ui_Send):
    def __init__(self, app, dbc):
        super(sendLayoutClass, self).__init__()
        self.setupUi(self)
        self.set_logo()
        self.app = app
        self.dbc = dbc
        self.logo_btn.clicked.connect(self.close)
        self.excel_btn.clicked.connect(self.send_excel)
        self.api_btn.clicked.connect(self.send_api)
        self.show_num_list()
        
        
    def show_num_list(self):
        query = "SELECT DATE, CAR_NO, SEND_YN FROM NUMBER WHERE SEND_YN = 0"
        rows = self.dbc.select(query)
        for row in rows:
            self.number_list.append(row['car_no'])
    
    def send_excel(self):
        excel = makeExcelClass(self.dbc)
        excel.make_excel()
    
    def send_api(self):
        query = "SELECT API_PATH FROM SETTING"
        rows = self.dbc.select(query)
        api_path = rows[0]['api_path']
        try:
            data = json.dumps({"vehicles": rows}, ensure_ascii=False)
            headers = {'Content-Type': 'application/json'}
            response = requests.post(api_path, data=data, headers=headers)
            
            if response.status_code == 200:
                print('데이터 전송 성공:', response.json())
            else:
                print('데이터 전송 실패:', response.status_code, response.text)
        except Exception as ex:
            print(f'Send Api Error: {ex}')
