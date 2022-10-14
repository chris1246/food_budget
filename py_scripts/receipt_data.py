import PyPDF2
from datetime import datetime
import re
import os
import json

class reader():
    def __init__(self)->None:
        self.json_file = 'srch_parameters.json'
        with open('srch_parameters.json') as f:
            self.search_parameters = json.load(f)
        self.search_list = []
        self.on_line = []
        
        

    def reciever(self, insertion_data, sender, path):
        self.sender = sender
        #print(self.sender[0])
        pdfFile = f"{path}/{insertion_data}"
        pdfRead = PyPDF2.PdfFileReader(pdfFile)
        page = pdfRead.getPage(0)
        self.pageContent = page.extractText()
        os.remove(f"{path}/{insertion_data}")
        self.lines = self.pageContent.split('\n')
        #for i in range(len(self.lines)):
        #   print(self.lines[i])
        self.status = 0
        self.identifier()
        if(len(self.items_found) > 0):

            self.data_reader()
        else:
            print("no stores found")
            self.parameters_creator()

    def identifier(self):
        txt_line = self.lines
        self.items_found = []
        if self.status == 0:
            keyword = list(self.search_parameters['stores'])
            for line in range(len(txt_line)):                   
                for keywords in range(len(keyword)):
                    initiate = re.search(keyword[keywords].lower(), txt_line[line].lower())
                    print(f"Searched: {txt_line[line].lower()} for {keyword[keywords]}")
                    if initiate:
                        self.items_found.append(keyword[keywords])
                        print(f"Keyword {keyword[keywords]}, found on line {line}, with text: '{txt_line[line]}'")
                        self.item = keyword[keywords]
        else:
            keyword = self.search_list[0]
            for line in range(len(txt_line)):
                initiate = re.search(keyword.lower(), txt_line[line].lower())
                print(f"Searched: {txt_line[line].lower()} for {keyword.lower()}")
                if initiate:
                    self.items_found.append(keyword)
                    self.on_line.append(line)
                    print(f"Keyword {keyword}, found on line {line}, with text: '{txt_line[line]}'")
                    self.item = keyword
                    

    def data_reader(self):
        self.items_found.clear()
        print(f"Store: {self.item}")

    def store_creator(self):
        store_name = input("Input name of store: ")
        self.search_list.append(store_name)
        self.status = 1
        self.identifier()
        self.search_list.clear()
        print(self.items_found)
        if(len(self.items_found) > 0):
            print(f"Found {len(self.items_found)} examples of {store_name}")

            #current_keywords = self.search_parameters['stores']
            #print(current_keywords)
            #current_keywords.append(f"{store_name}")
            #print(current_keywords)
            #print(json.dumps(self.search_parameters))
            #json.dump(current_keywords, self.json_file)
            #with open(self.json_file, 'w') as out_file:
            #    out = json.dumps(self.search_parameters)
            #    out_file.write(out)

            self.store_name = store_name

            self.parameters_creator()


            
        elif(len(self.items_found) == 0):
            print(f"No examples found with: {store_name}, try again")
            
            self.store_creator()



    def parameters_creator(self):
        indexes = ['Input name of store: ','Enter the name of the first item: ', 'Enter the name of the last item: ']
        self.parameters = []
        
        for i in range(3):
            initial_search = input(f"{indexes[i]}")
            self.search_list.append(initial_search)
            self.status = 1
            self.identifier()
            self.search_list.clear()
            print(self.items_found)
            if(len(self.items_found) > 0):
                print(f"Found {len(self.items_found)} examples of {initial_search}")

                #current_keywords = self.search_parameters['stores']
                #print(current_keywords)
                #current_keywords.append(f"{initial_search}")
                #print(current_keywords)
                #print(json.dumps(self.search_parameters))
                #json.dump(current_keywords, self.json_file)
                #with open(self.json_file, 'w') as out_file:
                #    out = json.dumps(self.search_parameters)
                #    out_file.write(out)
                self.parameters.append(initial_search)
                #self.store_name = store_name
                #self.start

            elif(len(self.items_found) == 0):
                print(f"No examples found with: {initial_search}, try again")
                
                self.parameters_creator()
            
                #enter first item
                #enter last item
        print(self.parameters)
        
        
