import mysql.connector as mariadb

class gateway():
    def __init__(self) -> None:
        self.mariadb_connection = mariadb.connect(user='local2', 
                                    password='0000', 
                                    database='home_assistant', 
                                    host='10.209.154.141', 
                                    port='3306')
        self.create_cursor = self.mariadb_connection.cursor()

    def upload(self, print_data, table):
        sql_statement = f'INSERT INTO {0} (COLUMN1, COLUMN2) VALUES ("hi",5), ("hi",6)';
        self.create_cursor.execute(sql_statement)
        self.mariadb_connection.commit();
        
        
        self.mariadb_connection.close()
        return f"{print_data}"

        
