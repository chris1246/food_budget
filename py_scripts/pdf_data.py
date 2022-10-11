import PyPDF2
from datetime import datetime
import re



class reader():
    def __init__(self) -> None:
        self.search_dict = {}
        self.act_dict = {}
        self.search_words_dict = {}
        self.act_words_dict = {}
        self.li = []
        self.search_limit = 10
        self.lines_list = []
        self.adjust = 0
        pass

    def reciever(self, insertion_data, sender):
        self.sender = sender
        print(self.sender[0])
        self.status = True
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        pdfFile = f"{insertion_data}"
        pdfRead = PyPDF2.PdfFileReader(pdfFile)
        page = pdfRead.getPage(0)
        self.pageContent = page.extractText()
        
        self.find_store()


    def find_store(self):
        self.lines = self.pageContent.split('\n')
        foetex = "www.foetex.dk"
        foetex_ny = "Føtex"
        netto_skb = "Søtoften 2A"

        for i in range(len(self.lines)):
            self.search_dict[self.lines[i]] = f"{i}"
            self.act_dict[f"{i}"] = [self.lines[i]]
        
        for x in range(len(self.lines)):
            self.lines_list.append(self.lines[x])
        _ = []

        for store in range(len(self.lines)): #self.search_limit
            
            store_srch_foetex = re.search(foetex, self.lines[store])
            store_srch_netto = re.search(netto_skb, self.lines[store])
            store_search_foetex_ny = re.search(foetex_ny, self.lines[store])
            if store_srch_foetex:
                self.foetex()
                break
            if store_srch_netto:
                self.netto_skb()
                break
            if store_search_foetex_ny:
                self.foetex_ny()
                break
            if len(_) >= self.search_limit:
                print("store not found")
                break
            else:
                _.append("0")
                

    def netto_skb(self):
        find_key_min = "8660 Skanderborg"
        #print(self.search_dict)
        #print(self.lines_list)
        for min in range(int(len(self.lines_list))):
            min_srch = re.search(find_key_min, self.lines_list[min])
            if min_srch:
                break
        
        while self.status == True:
            for t in range(int(min)+1, len(self.act_dict)):
                txt = self.act_dict[f'{t}']
                #future = f"{self.act_dict[f'{i+1}']}"
                txtsrch = f"{txt}"
                tax = re.search("TOTAL", txtsrch)
                print(self.act_dict[f'{t}'])
                if tax:
                    self.status = False
                    break

    def foetex(self):
        find_key_min = '************************************'
        
        min = self.search_dict[find_key_min]

        

        while self.status == True:
            for i in range(int(min)+1, len(self.act_dict)):
                i = i + self.adjust
                self.adjust = 0
                txt = self.act_dict[f'{i}']
                future = f"{self.act_dict[f'{i+1}']}"
                future2 = f"{self.act_dict[f'{i+2}']}"
                txtsrch = f"{txt}"
                
                x = re.search("TOTAL", txtsrch)
                #y = re.findall('\d*\.?\d+',txtsrch)
                #print(f"{txt[0]}")

                regex = r"(\d+,\d\d)[^\d]*$"
                regex__cl = r"\d+,\d\d[^\d]*$"
                si_number = r"\d+"
                price = r"$"
                regex_ = "-"
                regex_cl = "RABAT"
                substr = ""
                total = "TOTAL"
                rec = "PANT"
                star_key = "\*"
                comma_key = "\,"
                comma_replace = "."
                isolate_number = r"-?\d+,\d{2}"


                title = re.sub(regex, substr, f"{txt[0]}", 1)
                number = re.search(regex, f"{txt[0]}")
                clearance_current = re.search(regex_cl, f"{txt[0]}")
                clearance = re.search(regex_, f"{self.act_dict[f'{i+1}']}", 1)
                clearance_srch = re.search(regex_cl, f"{self.act_dict[f'{i+1}']}")
                total_status = re.search(total, f"{txt[0]}")
                recycle = re.search(rec, f"{txt[0]}")
                #print(f"Rabatsøger -{self.act_dict[f'{i+1}']}-")
                if total_status:
                    self.status = False
                    break
                if recycle:
                    self.status = False
                    break
                if number:
                    if clearance_current:
                        pass
                    else:
                        if clearance_srch:
                            clearance_number = re.findall(regex__cl, future[2:int(len(future))-3])
                            if clearance_number:
                                print(f"Titel: {title}, Pris:{number[0]}, Rabat:{clearance_number[0]}, Butik:Føtex, Antal:X")
                        else:
                            print(f"Titel: {title}, Pris:{number[0]}, Rabat:0,00")
                else:
                    star = re.search(star_key, f"{txt[0]}")
                    if star:
                        pass
                    else:
                        amount_future = re.search(si_number, f"{self.act_dict[f'{i+1}']}")
                        price_future = re.search(regex, f"{self.act_dict[f'{i+1}']}")
                        if amount_future:
                            if price_future:
                                _ = f"{price_future[0]}"
                                rf = f"{_[0:int(len(_)-2)]}"
                                fuckcomma = re.sub(comma_key, comma_replace, rf, 1)
                                clearance_srch2 = re.search(regex_cl, f"{self.act_dict[f'{i+2}']}")
                                if clearance_srch2:
                                    clearance_number2 = re.findall(isolate_number, f"{self.act_dict[f'{i+2}']}")
                                    
                                    print(f"Titel: {title}, Pris:{float(fuckcomma)/float(amount_future[0])}, Rabat:{clearance_number2[0]}, Butik:Føtex, Antal:{amount_future[0]}")
                                    self.adjust = 1
                                else:
                                    print(f"Titel: {title}, Pris:{float(fuckcomma)/float(amount_future[0])}, Rabat:0,00 , Butik:Føtex, Antal:{amount_future[0]}")

                        else:
                            print("idfk")
                    pass
                if x:
                    self.status = False
                    break

    def foetex_ny(self):
        #for i in range(len(self.lines_list)):
        #    print(f"Linje: {i} - {self.lines_list[i]}")

        find_key_min = "Beskrivelse AntalPris"
        find_key_max = "I alt inkl. moms"


        #print(self.search_dict)
        #print(self.lines_list)
        for min in range(int(len(self.lines_list))):
            min_srch = re.search(find_key_min, self.lines_list[min])
            if min_srch:
                break

        for max in range(int(len(self.lines_list))):
            max_srch = re.search(find_key_max, self.lines_list[max])
            if max_srch:
                break
        print(max)

        
        for t in range(int(min)+1, int(max)):
            numb = r"\d{0,10}\.\d{0,10}(\.\d{1,2})?$" #https://stackoverflow.com/questions/24499906/i-need-this-regex-expression-to-allow-0-0-00-or-00-00
            clrnce = "Rabat"
            substr = ""
            amount = r"^\d{0,10}\.\d{2}"
            regex_cl = r"-?\d+\.\d{2}"
            #price = r"\d{0,10}(\.\d{1,2})?$"
            txt = self.act_dict[f'{t}']
            recycle = "PANT"
            

            future = f"{self.act_dict[f'{t+1}']}"
            txtsrch = f"{txt}"
            
            numbers = re.search(numb, f"{txt[0]}")
            clearance_current = re.search(clrnce, f"{txt[0]}")
            clearance_srch = re.search(clrnce, f"{self.act_dict[f'{t+1}']}")
            title = re.sub(numb, substr, f"{txt[0]}", 1)
            recycle = re.search(recycle, f"{txt[0]}")
            
            if numbers:
                price = re.sub(amount, substr, f"{numbers[0]}", 1)
                amount_s = re.search(amount, f"{numbers[0]}")
                if recycle:
                    price = "0.00"
                #print(numbers[0])
                
                if amount_s:
                    if clearance_current:
                        pass
                    else:   
                        if clearance_srch:
                            clearance_amount = re.search(numb, future[2:int(len(future))-2])
                            if clearance_amount:
                                #print(clearance_amount)
                                print(f"Titel: {title} \t Pris:{price} \t Rabat:{clearance_amount[0]} \t Butik:Føtex \t Antal:{amount_s[0]}")
                        else:
                            print(f"Titel: {title} \t Pris:{price} \t Rabat:0.00 \t Butik:Føtex \t Antal:{amount_s[0]}")
                else:
                    print("no amount")
            else:
                pass