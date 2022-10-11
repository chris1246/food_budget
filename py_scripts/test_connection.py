# File: test_connection.py     Function: test platform for oploading data through push.py   Type: script

from dataclasses import dataclass
import push
object = push.gateway()


#table = "python_creation_table"#
table = "test_table"
data = {'ID': 8, 'COLUMN1':'Alpha', 'COLUMN2': 'Beta'}
#data = {'COLUMN1':'hh', 'COLUMN2': 2}
print(object.verify(data, table))