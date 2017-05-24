from transfer_mod import check_updates, manual_updates, mod_time_display
from tkinter import *
from tkinter import ttk
from datetime import datetime,time,timedelta
import os


root = Tk()
src =("C:/Users/Santiago B/Desktop/python/py_practice/File transfer 3.0/file_A")
dst =("C:/Users/Santiago B/Desktop/python/py_practice/File transfer 3.0/file_B")
file_dirA = os.listdir('C:/Users/Santiago B/Desktop/python/py_practice/File transfer 3.0/file_A')
file_dirB = os.listdir('C:/Users/Santiago B/Desktop/python/py_practice/File transfer 3.0/file_B')

##mod_timeA = os.stat(file_dirA+'\\'+m).st_mtime
##mod_timeB = os.stat(file_dirB+'\\'+m).st_mtime

##Want to add time stamps next to file names so the changes are more noticable
## Visit transfer_mod and make a new function for just the time stamp to be imported

label = Label(root, text = "File updates")
label.grid(row = 0, column = 0) 

check = Button(root, text = "Check", command = manual_updates)
check.grid(row = 1, column = 0, rowspan = 2, columnspan = 2)

scroll_barA = Scrollbar(root)
scroll_barA.grid(row = 6, column = 3, columnspan = 2 )

scroll_barB = Scrollbar(root)
scroll_barB.grid(row = 6, column = 7, columnspan = 2)

fileA_label = Label(root, text = 'File A (Work Files)')
fileA_label.grid(row = 1, column = 3)
fileA_list = Listbox(root, xscrollcommand = scroll_barA.set)
fileA_list.grid(row = 2, column = 3, rowspan = 3, columnspan = 2)
for x in file_dirA:
    time = datetime.fromtimestamp(os.stat(src+"/"+x).st_mtime)
    fileA_list.insert(END, str(x)+' / '+str(time))
    

fileB_label = Label(root, text = 'File B (Backup files)')
fileB_label.grid(row = 1, column = 7)
fileB_list = Listbox(root, xscrollcommand = scroll_barB.set)
fileB_list.grid(row = 2, column = 7, rowspan = 3, columnspan = 2)
for x in file_dirB:
    time = datetime.fromtimestamp(os.stat(src+"/"+x).st_mtime)
    fileB_list.insert(END, str(x)+' / '+str(time))


scroll_barA.config(command = fileA_list.xview)
scroll_barB.config(command = fileB_list.xview)
mainloop()

