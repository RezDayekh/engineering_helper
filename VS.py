#RezeqAlla Dayekh. March 28, 2021.
#this is my first attempt to make a software that will help engineering become faster

#first we need to import the modules
#this module allows you to open web browser
import webbrowser
#the re is a module for regular expression
import re
#this module is used to deal with files and directories
import os
#this module made by myself to hold the functions and keep the main clean
from FunctionLib import Jobs
from graphics import *
from userInterface import *
import time
import pandas as pd


#path = 'C:\\Projects\\S\\SD#46 - Sunshine Coast\\kininnick scool\\1.20.8194.0 SD46 Kinnikinnick RTU Replace'
path = 'C:\\Projects\\L\\Langara College\\1.21.E068.0 Langara Bldg B Recommissioning'
#path = input('Please enter the file path: ')
#path = input('Enter Path here: ')
#path = 'C:\\Projects\\S\\SD#46 - Sunshine Coast\\Halfmoon Bay\\1.20.8226.0 SD46 Halfmoon Bay Elem UV Repl'
#so apparently you don't need the previous method i made. i will investigate further later today.
path = os.path.realpath(path)

job1 = Jobs(path)
job1.explore_directory(job1.job_path)
job1.set_default_quote()
job1.set_default_estiamte()



#here is my attempt to add graphics to the software
jobs_graphics_window = GraphWin('Jobs Documents', 500, 500)
jobs_graphics_window.setCoords(0,0,5,5)
jobs_graphics_window.setBackground('grey')

job_interface = JobInterface(jobs_graphics_window, job1)

job_interface.InterfaceDisplay()
job_interface.InterfaceStart()









#-----the following could be neccessary but its not used -----------
dict1 = {}
dict1['1'] = []
dict1['1'].append(1)
dict1['1'].append(2)
print(dict1['1'][1])

ls = [1,2]
ls.append('1')

#xls_file = pd.ExcelFile('Langara - Daycare RTU Replacement.xlsm')
#length = len(xls_file.sheet_names)


quote1_date = job1.quote_dict[0][2]
quote2_date = job1.quote_dict[1][2]
new_date = 'Mon Feb 25 09:56:29 2021'
if quote1_date > quote2_date:
    print('quote 1 bigger')

if new_date > quote1_date:
    print('new date bigger')

print(job1.shop_drawings_dict)
print(job1.estimate_dict)
print(job1.quote_dict)

#after this is were we call the funtions
os.startfile(fl.shop_drawings_dict['shops_1'])
path_insider = os.listdir(path)


#now we have to look inside the content of the path and get the engineering file
for content in path_insider:
    content_path = path + '\\' + content
    if os.path.isfile(content_path):
        #print('The following is a file', content)
        bla = 1
    if os.path.isdir(content_path):
        #print('The following is directory', content)
        bla = 1
    content_path = ''


#now we want to get the shop drawings
#we know the shop drawings will be in the engineering file
#so we look inside the engineering file and pick the file that have _SD
for content in path_insider:
    #this is the engineering file
    if content == 'Eng':
        engineering_path = path + '\\' + content
        engineering_content = os.listdir(engineering_path)
    #this is the estimate file
    if content == 'Est':
        estimate_path = path + '\\' + content
        estimate_content = os.listdir(estimate_path)

#trying to get the latest estimate
newest_estimate = 0
for estimate in estimate_content:
    if re.search('.+Estimate.+', estimate):
        #getting the time is not working. fix it please!
        #turns out it only needed the right path
        estimate_path = estimate_path + '\\' + estimate
        os.startfile(estimate_path)
        estimate_creation = time.ctime(os.path.getctime(estimate_path))
        #here is where we find the latest estimate
        if estimate_creation > newest_estimate:
            newest_estimate = estimate_creation
            correct_estimate = path + '\\' + estimate

os.startfile(correct_estimate)

#now trying to get the shop drawings
for files in engineering_content:
    if re.search('.+SD.+', files):
        shop_drawings = engineering_path + '\\' + files

    
#the following line open any document given the right path
os.startfile(shop_drawings)




