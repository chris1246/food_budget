from dataclasses import dataclass
import push
object = push.gateway()


table = "python_creation_table"
data = "hello world"
print(object.upload(data, table))