import mysql.connector as mariadb

class gateway():
    def __init__(self) -> None:
        mariadb_connection = mariadb.connect(user='local2', 
                                    password='0000', 
                                    database='home_assistant', 
                                    host='10.209.154.141', 
                                    port='3306')

    def upload(self):
        
