from datetime import datetime,time,timedelta
import shutil
import os
from tkinter import filedialog




#The addresses of the src file and dst file
src =("C:/Users/Santiago B/Desktop/python/py_practice/File transfer 3.0/file_A")
dst =("C:/Users/Santiago B/Desktop/python/py_practice/File transfer 3.0/file_B")

files_dir = os.listdir(src) #Gets the directory of the src
t = datetime.now()#gets current time

def check_updates():
    for m in files_dir:
        if m.endswith('.txt'): #Checks if the file is a .txt document
            files = (src+'\\'+m) #Stores the address of the text documents to use later
            mod_time_unix = os.stat(src+'\\'+m).st_mtime # Gets the unix time stamp
            mod_time = datetime.fromtimestamp(mod_time_unix) #converts this unix timestamp to a datetime object
            time_since_mod = (t - mod_time) # Gets the time diffrence between the current time and the time it was modified
            if time_since_mod < timedelta(days=1): # If time_since_mod is less than 1 day (meaning it was modified that day) -->
                shutil.copy(files,dst) # It copies the file to dst
                print(m, 'has been copied to ', dst)
            else:
                print("This file hasn't been changed: ", m)

def manual_updates():
    save =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print('Manulay updated')


def mod_time_display():
    for m in files_dir:
        if m.endswith('.txt'):
            files = (src+'\\'+m)
            mod_time_unix = os.stat(src+'\\'+m).st_mtime
            mod_time = datetime.fromtimestamp(mod_time_unix)
        print(mod_time)
        

check_updates()
            
            
