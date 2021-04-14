import tkinter as tk
from tkinter.ttk import Combobox
import time
from FunctionLib import *



class MainWindow:
    '''the main window will display the buttons and the jobs'''
    def __init__(self, root, all_jobs_info):
        self.jobs = all_jobs_info
        #starting the root window
        self.root = root
        self.main_jobs_list = []
        #adding the attributes of the main window
        #self.selection_label

        #we only want one addition window so we initiated it here
        self.entry_window = AdditionWindow(self.root)#,self.jobs_list)

    def initiate_the_window(self):
        '''call the displaying functions'''
        self.__create_top_frame()
        self.__create_bottom_frame()


    def __create_top_frame(self):
        '''this top frame will have the label, combobox
        and new job button, and maybe refesh button'''
        jobs_label = tk.Label(self.root, text='Select Job:')
        jobs_label.place(x=0, y=10)

        #this is the box that will display the jobs we will use
        
        #this list will have the jobs
        #quote_list = [111,222,333,444]
        self.job_choose_box = Combobox(self.root, values=self.main_jobs_list, state='normal', width=30)
        self.job_choose_box.place(x=65, y=10)
        self.job_choose_box.bind('<<ComboboxSelected>>')

        #this button will add a new job
        self.new_job_button = tk.Button(self.root, text='+', width=1, height = 1, command=self.__job_entry_window)
        self.new_job_button.place(x=275, y=7)

        self.new_job_button = tk.Button(self.root, text='update', width=5, height = 1, command=self.update_list)
        self.new_job_button.place(x=300, y=7)

    def update_list(self):
        self.main_jobs_list = self.entry_window.jobs_list
        self.job_choose_box['values'] = self.main_jobs_list
        print('hi')


    def __create_bottom_frame(self):
        '''this will create the files buttons'''
        shops_button = tk.Button(self.root, text='File', width = 8)
        shops_button.place(x=90, y=50)

        shops_button = tk.Button(self.root, text='Eweb', width = 8)
        shops_button.place(x=210, y=50)

        shops_button = tk.Button(self.root, text='Quote', width = 8)
        shops_button.place(x=30, y=100)

        shops_button = tk.Button(self.root, text='Estimate', width = 8)
        shops_button.place(x=150, y=100)

        shops_button = tk.Button(self.root, text='PO', width = 8)
        shops_button.place(x=270, y=100)

        shops_button = tk.Button(self.root, text='Engtool', width = 8)
        shops_button.place(x=30, y=150)

        shops_button = tk.Button(self.root, text='Shops', width = 8)
        shops_button.place(x=150, y=150)

        shops_button = tk.Button(self.root, text='As-Builts', width = 8)
        shops_button.place(x=270, y=150)

    def __job_entry_window(self):
        '''this will be called when you  press on the new job button
        that was created in create_top_frame
        it will create an entry job class'''
        #entry_window = AdditionWindow(self.root)#,self.jobs_list)
        self.entry_window.display_new_window()
        self.entry_window.initiate_attributes()
    

class AdditionWindow():
    '''this window will add the new jobs'''
    def __init__(self, root):#, all_jobs_list):
        self.jobs_list = []
        self.root = root

    def display_new_window(self):
        '''this function was added to display the addition window whenever the + button is pressed'''
        self.new_window = tk.Toplevel(self.root)
        self.new_window.resizable(width=False, height=False)
        self.new_window.title('Job Path and name')
        self.new_window.geometry('350x150+10+20')

    def initiate_attributes(self):
        '''this fucntion will initiate the window'''
        self.__enter_job_path()
        self.__enter_job_name()
        self.__enter_buttons()


    def __enter_job_path(self):
        '''this function will create the job path'''
        job_path_label = tk.Label(self.new_window, text='Job Path:')
        job_path_label.place(x=5, y=5)
        self.job_path_entry = tk.Entry(self.new_window)
        self.job_path_entry.place(x = 85, y =5, width=250)

    def __enter_job_name(self):
        '''this will create the job name'''
        job_name_label = tk.Label(self.new_window, text='Job Name:')
        job_name_label.place(x=5, y=50)
        self.job_name_entry = tk.Entry(self.new_window)
        self.job_name_entry.place(x = 85, y =50, width=250)

    def __enter_buttons(self):
        '''this will create the save and cancel button'''
        save_button = tk.Button(self.new_window, text='Save', width = 8, command=self.__get_job_info)
        save_button.place(x=85, y=100)

        cancel_button = tk.Button(self.new_window, text='Cancel', width = 8, command=self.__destroy_window)
        cancel_button.place(x=200, y=100)

    def __get_job_info(self):
        '''this function will get the job info from the entry objects'''
        self.job_name = self.job_name_entry.get()
        self.job_path = self.job_path_entry.get()
        self.__save_job_info()

    def __save_job_info(self):
        '''this function will get and save the job path to the jobs dictionary'''
        self.new_job = {} #a dictionary to hold the new job
        self.new_job[self.job_name] = Jobs(self.job_path, self.job_name)
        self.new_job[self.job_name].explore_directory(self.new_job[self.job_name].job_path)
        self.jobs_list.append(self.new_job)

        #self.jobs.jobs_dict[self.job_name] = self.job_path
        self.__destroy_window()

    def __destroy_window(self):
        '''will be called when save or cancel are hit'''
        self.new_window.destroy()