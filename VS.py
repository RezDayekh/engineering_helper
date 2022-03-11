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
from FunctionLib import *
from userInterface import *
import time
import pandas as pd

#import pyautogui as pag



#creating the jobs class
all_jobs = JobsData()

#Make the main window
root = tk.Tk()
root.resizable(width=False, height=False)

main_window = MainWindow(root,all_jobs)
main_window.initiate_the_window()

#main_window.start ?? maybe

root.title("Job Documents")
root.geometry('500x250+10+20')
root.mainloop()



