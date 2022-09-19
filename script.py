import requests as rq
from bs4 import BeautifulSoup as soup
import os
class gather():
    def __init__(self) -> None:
        self.namesList = []
        

        
    
    def get_files(self):
        try:
            self.files = [f for f in os.listdir('.') if os.path.isfile(f)]
        except BaseException as e:
            print(e, "An error happened in getting file names in the current directory- get_files Method")
            exit(1)
        return self.files


    def get_file_name(self, files, file_name = None, file_type = None): 
        """
        If you want to add a file name and/or file type/extension 
        you can add it in the file_name and file_type variables, 
        otherwise, it will automatically take the first html file in the
        current directory. 
        """
        if file_name == None and file_type == None:
        
            for f in files:
                if ".html" in f:
                    self.file = f
                    break
        
        elif file_type == None and file_name != None:
            for f in files:
                if str(file_name) in f:
                    self.file = f
                    break

        elif file_type != None and file_name == None:
            for f in files:
                if f".{file_type}" in f:
                    self.file = f
                    break
        else:
            self.file = f"{file_name}.{file_type}"
        
        return self.file
    
    def read_html(self, fileName):
        with open(str(fileName), 'r') as f:
            try:
                self.parsedHtml = soup(f, 'html.parser')
            except BaseException as e:
                print(e, "An error happened in parsing the read html content- read_html Method")
                exit(1)
        return self.parsedHtml
    
    def get_names(self, parsedText):

        try:
            for div in parsedText.find_all('div', role="listitem"):
                for span in div.find_all('span', class_ = 'zWGUib'):
                    name = span.text
                    self.namesList.append(name)
        except BaseException as e:
            print(e, "An error happened in while searching for the names inside the html content- get_names Method")
            exit(1)    
        return self.namesList
    
    def run(self):
        #Change file name or type if needed 
        self.parsedHtml = self.read_html(self.get_file_name(self.get_files(), file_name=None, file_type='html'))
        self.namesList = self.get_names(self.parsedHtml)

        return self.namesList
    
    def store(self):
        try:
            with open('attended.txt', 'w') as w:
                for name in self.run():
                    temp_list = (f"{name}\n".split("\n"))
                    final_name = ""
                    for n in temp_list:
                        final_name = final_name + " " +n.strip() 
                    w.write(f"{final_name}\n".strip(""))
        except BaseException as e:
            print(e, "An error happened in while writing the names in a text file- store Method")
            exit(1)    
            


obj = gather()
obj.store()

