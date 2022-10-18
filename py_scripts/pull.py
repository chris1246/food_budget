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

    