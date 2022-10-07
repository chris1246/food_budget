# File: push.py     Function: db uploader   Type: script
# 
# Script input parameters:
#   object.verify(data, table)
#       table = "test_table"
#       data = {'ID': 3, 'COLUMN1':'Alpha', 'COLUMN2': 'Beta'}
#
#
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
        
    def verify(self, data, table): 
        columns = []
        columns_data = []
        #try:
        self.create_cursor.execute(f"SHOW COLUMNS FROM {table};")
        for x in self.create_cursor:
            columns.append(x[0])
            columns_data.append(x[1])
            
        if((len(data))!=len(columns)):
            print(f"Error: length of data ({len(data)}), and length of columns retrieved from Table ({len(columns)}) are not equal")
            raise                

        for i in range(len(data)): #validifies if integer expected, but none given    
            insertion__ = data[f'{columns[i]}']
            print(insertion__)
        
            if columns_data[i] == 'varchar(255)': #spaghetikode to be fixed
                if(type(insertion__) == int):
                    print(f"Error: Entered ({insertion__}) value for Column: ({columns[i]}) With datatype: ({columns_data[i]}), is an integer")
                    raise
                else:
                    pass

                if((len(insertion__)) > 255):
                    print(f"Error: Entered ({insertion__}) value for Column: ({columns[i]}) With datatype: ({columns_data[i]}), larger than 255")
                    raise
                else:
                    pass

            if columns_data[i] == 'varchar(2)': #spaghetikode to be fixed
                if(type(insertion__) == int):
                    print(f"Error: Entered ({insertion__}) value for Column: ({columns[i]}) With datatype: ({columns_data[i]}), is an integer")
                    raise
                else:
                    pass

                if((len(insertion__)) > 2):
                    print(f"Error: Entered ({insertion__}) value for Column: ({columns[i]}) With datatype: ({columns_data[i]}), larger than 2")
                    raise
                else:
                    pass


            if columns_data[i] == 'int(11)':
                if(type(insertion__) != int):
                    print(f"Error: Entered ({insertion__}) value for Column: ({columns[i]}) With datatype: ({columns_data[i]}), is not an integer")
                    raise
                else:
                    pass
        self.upload(data, table, columns, columns_data)       
        #except:
        #    return("Error")
    
    def upload(self, data, table, columns, columns_data): # Spaghetti monster: to be fixed
        print(columns_data)
        insertion = []
        for i in range(len(data)):
            print(data)
            print(columns)
            #print(data[f'{columns[i]}'])
            insertion.append(data[f'{columns[i]}'])

        print(insertion)
            
        if len(data) == 3:
            print("3 inputs")
            sql_statement = f'INSERT INTO {table} ({columns[0]}, {columns[1]}, {columns[2]}) VALUES ({insertion[0]}, "{insertion[1]}", "{insertion[2]}")';

        elif len(data) == 2:
            print("2 inputs")
            sql_statement = f'INSERT INTO {table} ({columns[0]}, {columns[1]}) VALUES ("{insertion[0]}", "{insertion[1]}")';
        else:
            raise("length of input not supported :(")
        print(sql_statement)
        self.create_cursor.execute(sql_statement)
    # print("3")
        self.mariadb_connection.commit();
        
        print("done")
        self.mariadb_connection.close()
        
        return("upload")

        
