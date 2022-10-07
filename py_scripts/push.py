import mysql.connector as mariadb
import json

class gateway():
    def __init__(self) -> None:
        a = ['user', 'password', 'database', 'host', 'port']
        credentials = []
        with open('connection_parameters.json') as f:
            data = json.load(f)
        for i in range(len(data)):
            credentials.append(data[a[i]])
        
        
        
        self.mariadb_connection = mariadb.connect(user=f'{credentials[0]}', 
                                    password=f'{credentials[1]}', 
                                    database=f'{credentials[2]}', 
                                    host=f'{credentials[3]}', 
                                    port=f'{credentials[4]}')
        self.create_cursor = self.mariadb_connection.cursor()
        
        

    def upload(self, print_data, table):
        sql_statement = f'INSERT INTO {table} (COLUMN1, COLUMN2) VALUES ("hi",5), ("hi",6)';
        self.create_cursor.execute(sql_statement)
        self.mariadb_connection.commit();
        
        
        self.mariadb_connection.close()
        
        return f"{print_data}"

        
