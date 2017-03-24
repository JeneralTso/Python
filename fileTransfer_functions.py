from os import listdir, path, remove
from datetime import datetime
from time import mktime
from tkinter import *
from tkinter import filedialog
from shutil import copy

import fileTransfer_main
import fileTransfer_gui

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

# transfer files if created or modified within 24 hrs
time_now = datetime.now()
time_now_epoch = mktime(time_now.timetuple())
timeframe = 86400 #seconds in 24 hours
   
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

def clear(self):
    self.field_src.delete(0,END)
    self.field_dest.delete(0,END)
    self.listbox.delete(0,END)


if __name__ == "__main__":
    pass
