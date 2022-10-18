import PyPDF2
from datetime import datetime
import re
import os
import json
import create_parameters

class reader():
    def __init__(self)->None:
        self.json_file = 'srch_parameters.json'
        with open('srch_parameters.json') as f:
            self.search_parameters = json.load(f)
        self.search_list = []
        self.on_line = []
        self.words = [] #nested list
        self.redirect = create_parameters.creator()
        
    def reciever(self, insertion_data, sender, path):
        self.sender = sender
        _ = []
        #print(self.sender[0])
        pdfFile = f"{path}/{insertion_data}"
        pdfRead = PyPDF2.PdfFileReader(pdfFile)
        page = pdfRead.getPage(0)
        self.pageContent = page.extractText()
        os.remove(f"{path}/{insertion_data}")
        self.lines = self.pageContent.split('\n')
        for lines in range(len(self.lines)):
            self.words.append(self.lines[lines].split(' '))
        print(self.words)
        for t in range(len(self.lines)):
            print(f"Line: {t}: {self.lines[t]}")
        self.status = 0
        self.store_identifier()
        if(len(self.items_found) > 0):
            self.data_reader()
        else:
            print("no stores found")
            self.redirect.parameters_creator(self.lines, self.items_found, self.words)
            #self.parameters_creator()

    def store_identifier(self):
        txt_line = self.lines
        
        self.items_found = []
        if self.status == 0:
            keyword = list(self.search_parameters['stores'])
            for line in range(len(txt_line)):                   
                for keywords in range(len(keyword)):
                    initiate = re.search(keyword[keywords].lower(), txt_line[line].lower())
                    #print(f"Searched: {txt_line[line].lower()} for {keyword[keywords]}")
                    if initiate:
                        self.items_found.append(keyword[keywords])
                        #print(f"Keyword {keyword[keywords]}, found on line {line}, with text: '{txt_line[line]}'")
                        self.item = keyword[keywords]
    def data_reader(self):
        self.items_found.clear()
        print(f"Store: {self.item}")