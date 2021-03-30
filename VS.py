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
import FunctionLib as fl

import time


path = 'C:\\Projects\\S\\SD#46 - Sunshine Coast\\kininnick scool\\1.20.8194.0 SD46 Kinnikinnick RTU Replace'
#path = input('Please enter the file path: ')

#so apparently you don't need the previous method i made. i will investigate further later today.
path = os.path.realpath(path)
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
        #getting the time is not working. fix it!
        estimate_creation = time.ctime(os.path.getctime(estimate))
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




