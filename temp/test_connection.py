from dataclasses import dataclass
import py_scripts.push as push
object = push.gateway()


table = "python_creation_table"
data = "hello world"
print(object.upload(data, table))