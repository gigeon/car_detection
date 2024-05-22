import logging
import sqlite3
import os

# db_path = os.path.abspath(os.path.dirname(__file__))
db_path = ":memory:"
file_logger = logging.getLogger("log")

class DBController:
    
    con = None
    cur = None
    
    def __init__(self):
        try:
            self.con = sqlite3.connect(db_path)
            self.cur = self.con.cursor()

            self.check_table()
        except Exception as ex:
            file_logger.error("SQL init ERROR : {}".format(ex))
            
    def check_table(self):
        try:
            ...
        except Exception as ex:
            file_logger.error("SQL check_table ERROR : {}".format(ex))
        
    def insert(self, sql):
        try:
            ...
        except Exception as ex:
            file_logger.error("SQL insert ERROR : {}".format(ex))
        
    def delelte(self, sql):
        try:
            ...
        except Exception as ex:
            file_logger.error("SQL delete ERROR : {}".format(ex))
    
    def update(self, sql):
        try:
            ...
        except Exception as ex:
            file_logger.error("SQL update ERROR : {}".format(ex))
        
    def close(self, sql):
        try:
            ...
        except Exception as ex:
            file_logger.error("SQL close ERROR : {}".format(ex))
        
    def select(self, sql):
        try:
            ...
        except Exception as ex:
            file_logger.error("SQL select ERROR : {}".format(ex))

        
    def create_table(self):
        try:
            self.cur.execute("CREATE TABLE CONFIG(SPOT_ID text, USER_ID text, USER_PWD text)")
            self.cur.execute("CREATE TABLE NUMBER(CAR_NO text, PWD, text)")
            
        except Exception as ex:
            file_logger.error("SQL create table ERROR : {}".format(ex))