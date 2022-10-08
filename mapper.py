# File: mapper.py     Function: not in use   Type: script
import mysql.connector as mariadb


a = ['user', 'password', 'database', 'host', 'port']
credentials = []
with open('connection_parameters.json') as f:
    data = json.load(f)
for i in range(len(data)):
    credentials.append(data[a[i]])

mariadb_connection = mariadb.connect(user=f'{credentials[0]}', 
                            password=f'{credentials[1]}', 
                            database=f'{credentials[2]}', 
                            host=f'{credentials[3]}', 
                            port=f'{credentials[4]}')
create_cursor = self.mariadb_connection.cursor()
create_cursor.execute("SHOW COLUMNS FROM Meals;")
#create_cursor.execute("SHOW TABLES;")
for x in create_cursor:
    print(x[0])