from os import listdir, path, remove
from datetime import datetime
from time import mktime
from tkinter import *
from tkinter import filedialog
from shutil import copy
import sqlite3

import fileTransfer2_main
import fileTransfer2_gui


conn = sqlite3.connect('dateTime.db')
c = conn.cursor()

time_now = datetime.now()
time_now_epoch = mktime(time_now.timetuple())
timeframe = 86400 #seconds in 24 hours


def create_table(self):
    c.execute('CREATE TABLE IF NOT EXISTS filechecks(datetime TEXT)')
    conn.commit

def show_datetime(self):
    print ('tralala')
    c.execute('SELECT * FROM filechecks ORDER BY datetime DESC LIMIT 1') 
##    dateTime = c.fetchone()  
##
##    #What if there is no data in the database? If statement...
##
##
##    dateTime_str = dateTime.strftime('%m-%d-%Y %H:%M:%S')
##    
##    self.dateTime.set(dateTime_str)

print ('trololo')

def send_datetime(self):
    c.execute('INSERT INTO filechecks (datetime) VALUES (?)',(time_now))
    conn.commit()
    #c.close()     
    #conn.close()  Put these two into some kind of on window close function.


def browseSrc(self):
    sourceDirectory = filedialog.askdirectory(initialdir="C:\\")
    self.srcDir.set(sourceDirectory)
    return

def browseDest(self):
    destDirectory = filedialog.askdirectory(initialdir="C:\\")
    self.destDir.set(destDirectory)
    return

def listFiles(self):
    sourceDir = self.srcDir.get()
    filesInDir = listdir(sourceDir)
    for filename in filesInDir:
        eachFile = path.join(sourceDir, filename)
        self.listbox.insert(0,eachFile)

# Transfer files if created or modified within 24 hrs
def transfer(self):
    sourceDir = self.srcDir.get()
    destDir = self.destDir.get()
    filesToTrans = listdir(sourceDir)
    for file in filesToTrans:
        origFile = path.join(sourceDir, file)
        timestamp = path.getmtime(origFile)
        if (time_now_epoch - timestamp) <= timeframe:
            copy(origFile, destDir)
            remove(origFile)
    messagebox.showinfo(title='Success!',message='Your files have been transferred. \nHave a wonderful day. :-)')
    send_datetime()

# Clear all fields    
def clear(self):
    self.field_src.delete(0,END)
    self.field_dest.delete(0,END)
    self.listbox.delete(0,END)
    

if __name__ == "__main__":
    pass
