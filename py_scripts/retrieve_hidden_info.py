import json

class json_data():
    def __init__(self) -> None:
        with open('connection_parameters.json') as f:
            data = json.load(f)
        for i in range(len(data)):
            self.credentials.append(data[a[i]])
        
    def retrieve(self, input):
        if(input == 'user'):
            return(self.data[0])
        elif(input == 'password'):
            return(self.data[1])
        elif(input == 'database'):
            return(self.data[2])
        elif(input == 'host'):
            return(self.data[3])
        elif(input == 'port'):
            return(self.data[4])
        
        
        
        else:
            return("Failed")