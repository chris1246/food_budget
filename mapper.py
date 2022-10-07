#
#
#
#
#
import mysql.connector as mariadb
mariadb_connection = mariadb.connect(user='local2', password='0000', database='home_assistant', host='10.209.154.141', port='3306')
create_cursor = mariadb_connection.cursor()
create_cursor.execute("SHOW COLUMNS FROM Meals;")
#create_cursor.execute("SHOW TABLES;")
for x in create_cursor:
    print(x[0])