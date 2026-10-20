import MySQLdb
import os
from dotenv import load_dotenv

load_dotenv()

class MysqlConnect:
    def __init__(self):
        self.host = os.getenv("DATABASE_HOST")
        self.username = os.getenv("DATABASE_USERNAME")
        self.password = os.getenv("DATABASE_PASSWORD")
        self.name = os.getenv("DATABASE_NAME")
        self.db = MySQLdb.connect(
            host = self.host ,
            user = self.username ,
            passwd = self.password,
            db = self.name
        )
        self.cur = self.db.cursor()

  

