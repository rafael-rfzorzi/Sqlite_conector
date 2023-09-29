import sqlite3

class Bind_sqlite:
    def __init__(self):
        self.database_sql = ''
    def conect_db(self):
        self.conn = sqlite3.connect(self.database_sql)
        self.cursor = self.conn.cursor()
    def desconect_db(self):
        self.conn.close()