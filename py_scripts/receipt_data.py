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
        for t in range(len(self.lines)):
            print(f"Line: {t}: {self.lines[t]}")
        self.status = 0
        self.store_identifier()
        if(len(self.items_found) > 0):

            self.data_reader()
        else:
            print("no stores found")
            self.parameters_creator()

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
            
    def keyword_identifier(self):
        txt_line = self.lines
        keyword = self.search_list[0]

        self.srch_output = {}

        for line in range(len(txt_line)):
            initiate = re.search(keyword.lower(), txt_line[line].lower())
            #print(f"Searched: {txt_line[line].lower()} for {keyword.lower()}")
            if initiate:
                self.items_found.append(keyword)
                self.on_line.append(line)
                print(f"Keyword {keyword}, found on line {line}, with text: '{txt_line[line]}'")
                self.item = keyword


        txt_words = txt_line.split()

        for word in txt_words:
            print(f"Position: {word}, Word: {txt_words[word]}")
        


                    
                    

    def data_reader(self):
        self.items_found.clear()
        print(f"Store: {self.item}")

    def store_creator(self):
        store_name = input("Input name of store: ")
        self.search_list.append(store_name)
        self.status = 1
        self.keyword_identifier()
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
        entrys = ['Input name of store: ','Enter the name of the first item: ','Enter quantity of first item: ','Enter price of first item: ','Enter the name of the last item: ']
        for_dict = ['name_store', 'name_start', 'quantity', 'price', 'name_end']
        self.parameters = []
        parameters_dict = {}
        gathered_dict = {}

        txt_line = self.lines
        for i in range(len(entrys)):
            initial_search = input(f"{entrys[i]}")
            self.search_list.append(initial_search)

            self.status = 1
            self.keyword_identifier()
            self.search_list.clear()
            print(self.items_found)

            if(len(self.items_found) > 0):
                #print(f"Found {len(self.items_found)} examples of {initial_search}")
                gathered_dict[f'{for_dict[i]}'] = self.items_found
                print(f'Dict: {gathered_dict}')


                if i == 1:
                    #index_range = len[self.on_line]
                    line_srch = self.on_line[len(self.on_line)-1]
                if i == 2:
                    for i in range(len(txt_line)): 
                        srch_proximity = re.search(initial_search.lower(), txt_line[line_srch].lower())
                        if srch_proximity:
                            amount = i
                            parameters_dict['line'] = self.lines[line_srch]
                            print(f"Found {initial_search} on same line +{amount} as first item")
                            words_for_line = txt_line[line_srch].split()
                            for words in range(len(words_for_line)):
                                extract_item = re.search(initial_search, words_for_line[words])
                                extract_quantity = re.search(initial_search.lower(), txt_line[line_srch].lower())
                                if srch_proximity:
                                    parameters_dict['item'] = words_for_line[words]
                                    parameters_dict['item_loc'] = words
                                if extract_quantity:
                                    parameters_dict['quant'] = words_for_line[words]
                                    parameters_dict['quant_loc'] = words
                                print(parameters_dict)
                        break

                self.parameters.append(initial_search)
            elif(len(self.items_found) == 0):
                print(f"No examples found with: {initial_search}, try again")
                
                self.parameters_creator()
            
                #enter first item
                #enter last item
        start_line = self.on_line[1]
        print(f"start_line{start_line}")
        end_line = self.on_line[4]
        print(f"end_line{end_line}")

        print(self.parameters)
        current_keywords = self.search_parameters['stores']
        print(current_keywords)
        print(self.on_line)
        if start_line > end_line:
            print("Error, Last item initiated before first item")
            self.parameters_creator()

        
        
        
        
        
        
        
