from dataclasses import dataclass
import push
object = push.gateway()

data = "hello world"
print(object.upload(data))