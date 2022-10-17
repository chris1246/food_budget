import re
import json

class creator():
    def __init__(self) -> None:
        self.json_file = 'srch_parameters.json'
        with open('srch_parameters.json') as f:
            self.search_parameters = json.load(f)
        self.search_list = []
        self.on_line = []
        self.words = [] #nested list
    
    def parameters_creator(self, lines, items_found, words):
        self.items_found = items_found
        self.lines = lines
        self.words = words
        entrys = ['Input name of store: ','Enter the name of the first item: ','Enter quantity of first item (if not marked, leave empty): ','Enter price of first item: ','Enter the name of the last item: ']
        for_gathered_dict = ['name_store', 'name_start', 'quantity', 'price', 'name_end']
        for_loc_dict = [['line_for_store', 'word_for_store'],['line_for_item','word_for_item'],['line_for_quantity','word_for_quantity'],['line_for_price','word_for_price'],['line_for_last','word_for_last']]
        self.parameters = []
        parameters_dict = {}
        gathered_dict = {}
        loc_dict = {}

        txt_line = self.lines
        for i in range(len(entrys)):
            initial_search = input(f"{entrys[i]}")
            self.search_list.append(initial_search)
            self.status = 1
            self.keyword_identifier()
            self.search_list.clear()
            print(self.items_found)
            if(len(self.items_found) > 0):
                gathered_dict[f'{for_gathered_dict[i]}'] = self.words[self.words_dict['line']][self.words_dict['word_num']]
                print(f'Dict: {gathered_dict}')
                criteria = [self.words_dict['line'], self.words_dict['word_num']]
                for pos in range(2):
                    loc_dict[for_loc_dict[i][pos]] = criteria[pos]   
                
                self.parameters.append(initial_search)
            elif(len(self.items_found) == 0):
                print(f"No examples found with: {initial_search}, try again")
                self.parameters_creator()
        
        start = self.lines[loc_dict['line_for_item']-1]
        end = self.lines[loc_dict['line_for_last']+1]
        diff_itemq = loc_dict['word_for_quantity'] - loc_dict['word_for_item']
        diff_itemp = loc_dict['word_for_price'] - loc_dict['word_for_item']
        
        parameters_dict = {'search_start': start, 'search_end': end[0:16], 'item_to_q_diff': diff_itemq, 'item_to_p_diff': diff_itemp}
        store = f'{gathered_dict["name_store"]}'
        print(parameters_dict)

        start_line = loc_dict['line_for_item']
        end_line = loc_dict['line_for_last']

        if start_line > end_line:
            print("Error, Last item initiated before first item")
            self.parameters_creator()
        else:
            self.upload_to_json(store, parameters_dict)

                        
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
                self.words_finder(line, keyword)
                


    def store_creator(self):
        store_name = input("Input name of store: ")
        self.search_list.append(store_name)
        self.status = 1
        self.keyword_identifier()
        self.search_list.clear()
        print(self.items_found)
        if(len(self.items_found) > 0):
            print(f"Found {len(self.items_found)} examples of {store_name}")
            self.store_name = store_name
            self.parameters_creator()     
        elif(len(self.items_found) == 0):
            print(f"No examples found with: {store_name}, try again")
            
            self.store_creator()

    def words_finder(self, line, keyword):
        self.words_dict = {}
        for num in range(len(self.words[line])):
            find_word = re.search(keyword, self.words[line][num].lower())
            if find_word:
                self.words_dict['line'] = line
                self.words_dict['word_num'] = num

    def upload_to_json(self, store, dict):
        current_keywords = self.search_parameters['stores']
        print(current_keywords)
        current_keywords[store] = dict
        print(current_keywords)
        print(json.dumps(self.search_parameters))
        #json.dump(current_keywords, self.json_file)
        with open(self.json_file, 'w') as out_file:
            out = json.dumps(self.search_parameters)
            out_file.write(out)