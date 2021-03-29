#RezeqAlla Dayekh. March 28, 2021.
#this is my first attempt to make a software that will help engineering become faster

#first we need to import the modules

#this module allows you to open web browser
import webbrowser
#the re is a module for regular expression
import re
#this module is used to list the content of a directory
import os

import FunctionLib as fl

#print('C:\Projects\S\SD#46 - Sunshine Coast\kininnick scool\1.20.8194.0 SD46 Kinnikinnick RTU Replace')
path = 'C:\Projects\S\SD#46 - Sunshine Coast\kininnick scool\1.20.8194.0 SD46 Kinnikinnick RTU Replace'

new_path = fl.fix_path(path)


print(os.listdir(new_path))

