import json

class json_data():
    def __init__(self) -> None:
        with open('connection_parameters.json') as f:
            self.data = json.load(f)      
        
    def retrieve(self, input):
        return(self.data[input])
