import logging
import sqlite3
import os


file_logger = logging.getLogger("log")

class DBController:
    
    con = None
    cur = None
    
    def __init__(self):
        try:
            db_path = os.path.abspath(os.path.join(__file__, os.pardir,"car.dat"))
            # db_path = ":memory:" # 메모리에 DB 저장
            self.con = sqlite3.connect(db_path, check_same_thread = False)
            self.cur = self.con.cursor()

            self.check_table()

        except Exception as ex:
            file_logger.error("SQL init ERROR : {}".format(ex))
            
    def check_table(self):
        try:
            table_list = ["CONFIG", "NUMBER","SETTING"]
            self.cur.execute("SELECT name FROM sqlite_master")
            result = []
            
            for row in self.cur.fetchall():
                result.append(row[0])
                
            table_list.sort()
            result.sort()
            
            if table_list != result :
                for tableName in table_list:
                    if tableName not in result:
                        self.create_table(tableName)
        
            if len(self.select("SELECT * FROM CONFIG")) <= 0:
                self.insert_default_config()
            
            if len(self.select("SELECT * FROM SETTING")) <= 0:
                self.insert_default_setting() 
            
        except Exception as ex:
            file_logger.error("SQL check_table ERROR : {}".format(ex))
        
    def insert_default_config(self):
        try:
            query = "INSERT INTO CONFIG VALUES ('testId', '환경산업연구단지', 'a', 'a')"
            self.insert(query)
            
        except Exception as ex:
            file_logger.error("SQL insert_default_config ERROR: {}".format(ex))    
        
    def insert_default_setting(self):
        try:
            query = "INSERT INTO SETTING VALUES ('1234', 'C:/', 'https://hows.or.kr/api/terminal')"
            self.insert(query)
        except Exception as ex:
            file_logger.error("SQL insert_default_setting ERROR {}".format(ex))
        
    def insert(self, query):
        try:
            self.cur.execute(query)
            self.con.commit()
            
        except Exception as ex:
            file_logger.error("SQL insert ERROR : {}".format(ex))
        
    def delelte(self, query):
        try:
            self.cur.execute(query)
            self.con.commit()
        except Exception as ex:
            self.con.rollback()
            file_logger.error("SQL delete ERROR : {}".format(ex))
    
    def update(self, query):
        try:
            self.cur.execute(query)
            self.con.commit()
        except Exception as ex:
            file_logger.error("SQL update ERROR : {}".format(ex))
        
    def close(self, query):
        self.cur.close()
        self.con.close()

    def select(self, query):
        try:
            self.cur.execute(query)
            columns = [str(column[0]).lower() for column in self.cur.description]  # 컬럼명
            results = []
            for row in self.cur.fetchall():
                results.append(dict(zip(columns, row)))

            return results
            
        except Exception as ex:
            file_logger.error("SQL select ERROR : {}".format(ex))

        
    def create_table(self, tableName):
        create_querys = {
            "CONFIG": "CREATE TABLE CONFIG(\
                SPOT_ID NOT NULL PRIMARY KEY,\
                SPOT_NAME TEXT,\
                USER_ID TEXT NOT NULL,\
                USER_PWD TEXT NOT NULL)",
            "NUMBER": "CREATE TABLE NUMBER(\
                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
                DATE TEXT,\
                CAR_NO TEXT,\
                SEND_YN INTEGER DEFAULT 0)",
            "SETTING": "CREATE TABLE SETTING(\
                ADMIN_PWD TEXT,\
                SAVE_PATH TEXT,\
                API_PATH TEXT)",
        }
        try:
            self.cur.execute(create_querys[tableName])
            
            # # 테이블 생성 되었는지 확인(SELECT)
            # self.cur.execute(
            #     "SELECT name FROM sqlite_master WHERE name = '{}'".format(tableName)
            # )
            # results = self.cur.fetchone()
            # if results[0] == tableName:
            #     pass
            # else:
            #     raise Exception("Can't Created [{}] Table.")
        except Exception as ex:
            file_logger.error("SQL create table ERROR : {}".format(ex))