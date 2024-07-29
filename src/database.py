import sqlite3
from sqlite3 import Connection

class Database:
    def __init__(self) -> None:
        self.__connection_string = "daily_diet.db"
        self.conn = None

    def connect(self) -> None:
        self.__conn = sqlite3.connect(self.__connection_string)

    def get_connection(self) -> Connection:
        return self.__conn
    
db = Database()