from transfer_mod import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime,time,timedelta
import os


root = Tk()

def pick_fileA():
    global doc_nameA
    fileA = filedialog.askdirectory()
    doc_nameA = os.listdir(fileA)

def pick_fileB():
    global doc_nameB
    fileB = filedialog.askdirectory()
    doc_nameB = os.listdir(fileB)

def show_nameA():
    for x in doc_nameA:
        #time = datetime.fromtimestamp(os.stat(fileA+"/"+x).st_mtime)
        fileA_list.insert(END, str(x))

def show_nameB():
    for x in doc_nameB:
        #time = datetime.fromtimestamp(os.stat(fileA+"/"+x).st_mtime)
        fileB_list.insert(END, str(x))
##fileA = filedialog.askdirectory()
##print (fileA)
##doc_nameA = os.listdir(fileA)
##fileB = filedialog.askdirectory()
##print (fileB)
##doc_nameB = os.listdir(fileB)
#save =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))


##mod_timeA = os.stat(file_dirA+'\\'+m).st_mtime
##mod_timeB = os.stat(file_dirB+'\\'+m).st_mtime

##Want to add time stamps next to file names so the changes are more noticable
## Visit transfer_mod and make a new function for just the time stamp to be imported

label = Label(root, text = "File updates")
label.grid(row = 0, column = 0) 

work_file = Button(root, text = "Work file", command = pick_fileA)
work_file.grid(row = 1, column = 0, rowspan = 2, columnspan = 2)

work_file_show = Button(root, text = "Work file show", command = show_nameA)
work_file_show.grid(row = 3, column = 0, rowspan = 2, columnspan = 2)

backup_file = Button(root, text = "Back up file", command = pick_fileB)
backup_file.grid(row = 2, column = 0, rowspan = 2, columnspan = 2)

backup_file_show = Button(root, text = "Back up File show", command = show_nameB)
backup_file_show.grid(row = 4, column = 0, rowspan = 2, columnspan = 2)

check = Button(root, text = "Save", command = manual_updates)
check.grid(row = 5, column = 0, rowspan = 2, columnspan = 2)

scroll_barA = Scrollbar(root)
scroll_barA.grid(row = 6, column = 3, columnspan = 2 )

scroll_barB = Scrollbar(root)
scroll_barB.grid(row = 6, column = 7, columnspan = 2)

fileA_label = Label(root, text = 'File A (Work Files)')
fileA_label.grid(row = 1, column = 3)
fileA_list = Listbox(root, xscrollcommand = scroll_barA.set)
fileA_list.grid(row = 2, column = 3, rowspan = 3, columnspan = 2)

    

fileB_label = Label(root, text = 'File B (Backup files)')
fileB_label.grid(row = 1, column = 7)
fileB_list = Listbox(root, xscrollcommand = scroll_barB.set,)
fileB_list.grid(row = 2, column = 7, rowspan = 3, columnspan = 2)




scroll_barA.config(command = fileA_list.xview)
scroll_barB.config(command = fileB_list.xview)
mainloop()

