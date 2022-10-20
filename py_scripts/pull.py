# File: pull.py     Function: db uploader   Type: script
# 
# Script input parameters:
#   object.verify(data, table)
#       table = "test_table"
#       data = {'ID': 3, 'COLUMN1':'Alpha', 'COLUMN2': 'Beta'}
#
# 

import mysql.connector as mariadb
import json
import retrieve_hidden_info

class gateway():
    def __init__(self) -> None:
        self.data = retrieve_hidden_info.json_data() 
        self.mariadb_connection = mariadb.connect(user=f'{self.data.retrieve("user")}', 
                                    password=f'{self.data.retrieve("password")}', 
                                    database=f'{self.data.retrieve("database")}', 
                                    host=f'{self.data.retrieve("host")}', 
                                    port=f'{self.data.retrieve("port")}')
        self.create_cursor = self.mariadb_connection.cursor()
        self.rettieve()

    def retrieve(self):
        sql_statement = 'SELECT * from test_table'
        self.create_cursor.execute(sql_statement)
        myresult = self.create_cursor.fetchall()#create_cursor.fetchall() #fetchone() 
        print(myresult)