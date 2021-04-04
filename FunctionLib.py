import pandas as pd
import os
import re
import time

#every job will be an instance of the class jobs
class Jobs:
    '''this class will initiate every job and store all of it's important data'''

    def __init__(self, job_path):
        self.job_path = job_path
        #the following dictionaries will hold the needed files
        self.shop_drawings_dict = {}
        self.shops_counter = 0

        self.default_estimate = ''
        self.estimate_dict = {}
        self.estimate_counter = 0

        self.po_dict = {}
        self.po_counter = 0

        self.default_quote = '' #assigned in set_defualt_quote
        self.quote_dict = {}
        self.quote_counter = 0

    def explore_directory(self, job_path):
        '''this function will loop through the content of a directory
        if a directory is found, it will call it self
        if a file is found, it will send it to classify_file'''
        dir_content = os.listdir(job_path)
        for content in dir_content:
            content_path = job_path + '\\' + content
            #check the type of the content to send to the right function
            if os.path.isfile(content_path):
                #send to classify_file
                self.classify_file(content_path)

            if os.path.isdir(content_path):
                #send to explore_directory
                self.explore_directory(content_path)


    def classify_file(self, x_file):
        '''this function will look into the file, decides if the file is needed and if so,
        put the file inside the right dictionary'''

        #before entering, only check pdf or xlsm files
        if re.search('.+pdf', x_file) or re.search('.+xlsm', x_file):

            #this is to find the shops
            if re.search('.+_SD.+', x_file):
                self.add_shops(x_file)

            #this is to find the estimate
            if re.search('.+xlsm', x_file):
                self.add_estimate(x_file)

            #this is to find the quote
            if re.search('.+[Qq]uote.+',x_file) and re.search('.+pdf', x_file):
                self.add_quote(x_file)

#========================== Shops ======================
    def add_shops(self, x_file):
        '''this function will append the shop drawings and its information to the dictionary'''
        self.shop_drawings_dict[self.shops_counter] = []
        self.shop_drawings_dict[self.shops_counter].append(x_file)
        #self.shop_drawings_dict[self.shops_counter].append(time.ctime(os.path.getctime(x_file)))
        self.shop_drawings_dict[self.shops_counter].append(os.path.getctime(x_file))
        self.shop_drawings_dict[self.estimate_counter].append(0)
        self.shops_counter += 1

#========================== Quote ======================
    def add_quote(self,x_file):
        '''this method will add the quotes and their info to the quote dictionary'''
        self.quote_dict[self.quote_counter] = []
        self.quote_dict[self.quote_counter].append(x_file)
        #self.quote_dict[self.quote_counter].append(time.ctime(os.path.getctime(x_file)))
        self.quote_dict[self.quote_counter].append(os.path.getctime(x_file))
        self.quote_dict[self.quote_counter].append(0)
        self.quote_counter += 1

    def set_default_quote(self):
        '''this function will loop through the quote dict and set a default quote'''
        #if there is only one quote, set as default
        latest_quote_time = 0
        if len(self.quote_dict) == 1:
            self.quote_dict[0][2] = 1
            self.default_quote = self.quote_dict[0][0]
        else:
            for i in range(0,len(self.quote_dict)):
                #if the path the quote contain booked, set the quote as default
                if re.search('.+[Bb]ooked.+', self.quote_dict[i][0]):
                    self.quote_dict[i][2] = 1
                    self.default_quote = self.quote_dict[i][0]
                    break
                #here we are comparing time of creation, the latest quote is the default
                else:
                    #find the quote with the latest creation time and set the time to the variable
                    if self.quote_dict[i][1] > latest_quote_time:
                        latest_quote_time = self.quote_dict[i][1]

            #loop through the dictionary again to set the default quote that matches the time.
            for j in range(0,len(self.quote_dict)):
                if latest_quote_time == self.quote_dict[j][1]:
                    self.quote_dict[j][2] = 1
                    self.default_quote = self.quote_dict[i][0]
                    break

    def dispaly_default_quote(self):
        '''this method will be called from the user interface to display the default quote'''
        os.startfile(self.default_quote)
                    
#========================== Estimate ======================
    def add_estimate(self, x_file):
        '''this function will add the estimate and its info to the estimate dictionary'''
        xls_file = pd.ExcelFile(x_file)
        xls_file_length = len(xls_file.sheet_names)
        if re.search('.+[Ee]stimate.+',x_file) or xls_file_length > 15:
            self.estimate_dict[self.estimate_counter] = []
            self.estimate_dict[self.estimate_counter].append(x_file)
            #self.estimate_dict[self.estimate_counter].append(time.ctime(os.path.getctime(x_file)))
            self.estimate_dict[self.estimate_counter].append(os.path.getctime(x_file))
            self.estimate_dict[self.estimate_counter].append(0)
            self.estimate_counter += 1

    def set_default_estiamte(self):
        '''this function will loop through the estimate dict and set a default estimate'''
        #if there is only one quote, set as default
        latest_estiamte_time = 0
        if len(self.estimate_dict):
            self.estimate_dict[0][2] = 1
            #self.default_estimate = self.estimate_dict[0][0]
        else:
            for i in range(0,len(self.estimate_dict)):
                #if the path the quote contain booked, set the quote as default
                if re.search('.+[Bb]ooked.+', self.estimate_dict[i][0]):
                    self.estimate_dict[i][2] = 1
                    self.default_estimate = self.estimate_dict[i][0]
                    break
                #here we are comparing time of creation, the latest quote is the default
                else:
                    #find the quote with the latest creation time and set the time to the variable
                    if self.estimate_dict[i][1] > latest_quote_time:
                        latest_quote_time = self.estimate_dict[i][1]

            #loop through the dictionary again to set the default quote that matches the time.
            for j in range(0,len(self.estimate_dict)):
                if latest_quote_time == self.estimate_dict[j][1]:
                    self.estimate_dict[j][2] = 1
                    self.default_estimate = self.estimate_dict[i][0]
                    break

    def display_default_estimate(self):
        '''this method will display the default estimate'''
        os.startfile(self.default_estimate)








#not so important methods
def explore_main_directory(main_path):
        '''this function will explore the main directory and classify the files and directories
        to send them to the right functions'''
        path = os.path.realpath(main_path)
        main_path_content = os.listdir(path)
        for content in main_path_content:
            content_path = path + '\\' + content

def fix_path(path):
    '''this function takes a string in raw format and fixes it to reference the right link'''
    split_the_path = path.split('\\')
    #check every split for the cahracter '\x01' 
    for one_split in split_the_path:
        if '\x01' in one_split:
            for char_in_split in one_split:
                if char_in_split == '\x01':
                    one_split = one_split.split(char_in_split)
                    split_the_path[-1] = one_split[0]
                    job_number = '1' + one_split[-1]
                    split_the_path.append(job_number)

    new_path = ''
    for i in range(0,len(split_the_path)):
        if split_the_path[i] != split_the_path[-1]:
            new_path = new_path + split_the_path[i] + '\\'
        else:
            new_path = new_path + split_the_path[i]

    return new_path