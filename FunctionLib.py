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
        self.estimate_dict = {}
        self.estimate_counter = 0
        self.po_dict = {}
        self.po_counter = 0
        self.quote_dict = {}
        self.quote_counter = 0


    def classify_file(self, x_file):
        '''this function will look into the file, decides if the file is needed and if so,
        put the file inside the right dictionary'''

        #this is to find the shops
        if re.search('.+_SD.+', x_file):
            self.shop_drawings_dict[self.shops_counter] = x_file
            self.shops_counter += 1

        #this is to find the estimate
        if re.search('.+xlsm', x_file):
            xls_file = pd.ExcelFile(x_file)
            xls_file_length = len(xls_file.sheet_names)
            if re.search('.+[Ee]stimate.+',x_file) or xls_file_length > 15:
                self.estimate_dict[self.estimate_counter] = x_file
                self.estimate_counter += 1

        #this is to find the quote
        if re.search('.+[Qq]uote.+pdf',x_file):
            self.quote_dict[self.quote_counter] = x_file
            self.quote_counter += 1

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