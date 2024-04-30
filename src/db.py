import mysql.connector

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                db='ferremax'
            )
        return cls._instance

    def get_connection(self):
        return self.connection
