import openpyxl
from datetime import datetime
import os


class makeExcelClass():
    def __init__(self, dbc):
        self.wb = openpyxl.Workbook()
        self.dbc = dbc
        self.wb.active.title = '차량리스트'
        self.column = ['사업장', '차량번호', '날짜']
        
    def make_excel(self):
        now = datetime.now().strftime('%Y-%m-%d')
        query = "SELECT * FROM SETTING"
        rows = self.dbc.select(query)
        save_path = rows[0]['save_path']
        excel_name = f'{save_path}차량리스트_{now}.xlsx'
        
        if os.path.exists(excel_name):
            self.wb.active.append(self.column)
            
            query = "SELECT SPOT_NAME FROM CONFIG"
            spot_name = self.dbc.select(query)[0]['spot_name']
            
            query = "SELECT ID, DATE, CAR_NO FROM NUMBER WHERE SEND_YN = 0"
            rows = self.dbc.select(query)
            for row in rows:
                car_no = row['car_no']
                date = row['date']
                exe_row = [spot_name, car_no, date]
                self.wb.active.append(exe_row)
            
            self.wb.save(excel_name)
            
            for row in rows:
                query = f"UPDATE NUMBER SET SEND_YN = 1 WHERE ID = {row['id']}"
                self.dbc.update(query)