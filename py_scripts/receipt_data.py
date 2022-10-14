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
        self.store_name_list = []
        

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
            self.store_creator()

    def identifier(self):
        txt_line = self.lines
        self.items_found = []
        if self.status == 0:
            keyword = self.search_parameters['stores']
            for line in range(len(txt_line)):
                for keywords in range(len(keyword)):
                    initiate = re.search(keyword[keywords], txt_line[line].lower())
                    print(f"Searched: {txt_line[line].lower()} for {keyword[keywords]}")
                    if initiate:
                        self.items_found.append(keyword[keywords])
                        print(f"Keyword {keyword[keywords]}, found on line {line}, with text: '{txt_line[line]}'")
                        self.item = keyword[keywords]
        else:
            keyword = self.store_name_list[0]
            for line in range(len(txt_line)):
                initiate = re.search(keyword, txt_line[line].lower())
                print(f"Searched: {txt_line[line].lower()} for {keyword}")
                if initiate:
                    self.items_found.append(keyword)
                    print(f"Keyword {keyword}, found on line {line}, with text: '{txt_line[line]}'")
                    self.item = keyword

    def data_reader(self):
        self.items_found.clear()
        print(f"Store: {self.item}")

    def store_creator(self):
        self.store_name = input("Input name of store: ")
        self.store_name_list.append(self.store_name)
        self.status = 1
        self.identifier()
        print(self.items_found)
        if(len(self.items_found) > 0):
            print(f"Found {len(self.items_found)} examples of {self.store_name}")

            current_keywords = self.search_parameters['stores']
            print(current_keywords)
            current_keywords.append(f"{self.store_name}")
            print(current_keywords)
            print(json.dumps(self.search_parameters))
            #json.dump(current_keywords, self.json_file)
            with open(self.json_file, 'w') as out_file:
                out = json.dumps(self.search_parameters)
                out_file.write(out)


            
        elif(len(self.items_found) == 0):
            print(f"No examples found with: {self.store_name}, try again")
            self.store_name_list.clear()
            self.store_creator()



        
            #enter first item
            #enter last item
        
        
