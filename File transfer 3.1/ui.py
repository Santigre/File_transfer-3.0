from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime,time,timedelta
import shutil
import os


root = Tk()
t = datetime.now()

def pick_fileA():
    global doc_nameA
    global fileA
    fileA = filedialog.askdirectory()
    doc_nameA = os.listdir(fileA)
    fileA_list.delete(0, END)# Just in case there is an other file being shown
    print(fileA)
    show_nameA()


def pick_fileB():
    global doc_nameB
    global fileB
    fileB = filedialog.askdirectory()
    doc_nameB = os.listdir(fileB)
    fileB_list.delete(0, END)# Just in case there is an other file being shown
    print(fileB)
    check_updates()
    show_nameB()

def show_nameA():
    for x in doc_nameA:
        fileA_list.insert(END, str(x))

def show_nameB():
    for x in doc_nameB:
        fileB_list.insert(END, str(x))

def check_updates():
    for m in doc_nameA:
        if m.endswith('.txt'): #Checks if the file is a .txt document
            files = (fileA+'\\'+m) #Stores the address of the text documents to use later
            mod_time = datetime.fromtimestamp(os.stat(files).st_mtime) #converts this unix timestamp to a datetime object
            time_since_mod = (t - mod_time) # Gets the time diffrence between the current time and the time it was modified
            if time_since_mod > timedelta(days=1): # If time_since_mod is less than 1 day (meaning it was modified that day) -->
                shutil.copy(files,fileB) # It copies the file to dst
                print(m, "has been backed up to: ", fileB)
                show_nameB()
                fileB_list.delete(0, END)
            else:
                print("This file hasnt been changed: ", m)

def manual_updates():
    for m in doc_nameA:
        if m.endswith('.txt'): #Checks if the file is a .txt document
            files = (fileA+'\\'+m) #Stores the address of the text documents to use later
            mod_time = datetime.fromtimestamp(os.stat(files).st_mtime) #converts this unix timestamp to a datetime object
            time_since_mod = (t - mod_time) # Gets the time diffrence between the current time and the time it was modified
            if time_since_mod != timedelta(seconds = 0): # If time_since_mod is less than 1 day (meaning it was modified that day) -->
                shutil.copy(files,fileB) # It copies the file to dst
                print(m, "has been backed up to: ", fileB)
                fileB_list.delete(0, END)
                show_nameB()

label = Label(root, text = "File updates")
label.grid(row = 0, column = 0) 

work_file = Button(root, text = "Work file", command = pick_fileA)
work_file.grid(row = 1, column = 0, rowspan = 2, columnspan = 2)


backup_file = Button(root, text = "Back up file", command = pick_fileB)
backup_file.grid(row = 2, column = 0, rowspan = 2, columnspan = 2)


check = Button(root, text = "Save", command = manual_updates)
check.grid(row = 5, column = 0, rowspan = 2, columnspan = 2)

##scroll_barA = Scrollbar(root)
##scroll_barA.grid(row = 6, column = 3, columnspan = 2 )
##
##scroll_barB = Scrollbar(root)
##scroll_barB.grid(row = 6, column = 7, columnspan = 2)

fileA_label = Label(root, text = 'File A (Work Files)')
fileA_label.grid(row = 1, column = 3)
fileA_list = Listbox(root)
fileA_list.grid(row = 2, column = 3, rowspan = 3, columnspan = 2)

    

fileB_label = Label(root, text = 'File B (Backup files)')
fileB_label.grid(row = 1, column = 7)
fileB_list = Listbox(root)
fileB_list.grid(row = 2, column = 7, rowspan = 3, columnspan = 2)



'''yscrollcommand = scroll_barA.set'''
##scroll_barA.config(command = fileA_list.yview)
##scroll_barB.config(command = fileB_list.yview)

mainloop()

