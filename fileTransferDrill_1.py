'''
Jenny Tso
Daily File Transfer Script Drill

'''

from datetime import datetime
from time import mktime
from os import listdir, path
from shutil import copy

time_now = datetime.now()
time_now_epoch = mktime(time_now.timetuple())
timeframe = 86400 #seconds in 24 hours

dir_files_all = "C:\Users\Student\Desktop\Folder A" #source folder
dir_files_transfer = "C:\Users\Student\Desktop\Folder B" #destination folder
files_all = listdir(dir_files_all)

#finds files that were created or modified within the last 24 hrs
#copies these files to a destination directory
def copyFiles():
    for files in files_all:
        each_file = path.join(dir_files_all, files)
        time_modified = path.getmtime(each_file)
        time_created = path.getctime(each_file)
        
        if (time_now_epoch - time_modified) <= timeframe:
            copy(each_file, dir_files_transfer)
            if (time_now_epoch - time_created) <= timeframe:
                copy(each_file, dir_files_transfer)

#lists copied files
def listFiles():
    copied_files = listdir(dir_files_transfer)
    for new_files in copied_files:
        print new_files

copyFiles()
print "The following files have been copied:\n"
listFiles()

    
    

