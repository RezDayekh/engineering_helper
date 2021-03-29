#RezeqAlla Dayekh. March 28, 2021.
#this is my first attempt to make a software that will help engineering become faster

#first we need to import the modules

#this module allows you to open web browser
import webbrowser
#the re is a module for regular expression
import re
#this module is used to list the content of a directory
import os

#print('C:\Projects\S\SD#46 - Sunshine Coast\kininnick scool\1.20.8194.0 SD46 Kinnikinnick RTU Replace')
path = 'C:\Projects\S\SD#46 - Sunshine Coast\kininnick scool\1.20.8194.0 SD46 Kinnikinnick RTU Replace'

#now that we have a better understanding of what is happening, let's do this
split_the_path = path.split('\\')
#check every split for the cahracter '\x01' 
for one_split in split_the_path:
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

print(os.listdir(new_path))
