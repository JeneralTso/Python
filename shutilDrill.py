'''
Jenny Tso
Python Shutil Module Drill

'''

import shutil
import os

src_FolderA = "C:\Users\Student\Desktop\Folder A"
dst_FolderB = "C:\Users\Student\Desktop\Folder B"
src_files = os.listdir(src_FolderA)
dst_files = os.listdir(dst_FolderB)

def copyDeleteFiles():
    for files in src_files:
        origFile = os.path.join(src_FolderA, files)
        if os.path.isfile(origFile):
            shutil.copy(origFile, dst_FolderB)
            os.remove(origFile)
            
    for copiedFiles in dst_files:
        eachCopiedFile = os.path.join(dst_FolderB, copiedFiles)
        print eachCopiedFile

print "The following files were successfully moved: \n"
copyDeleteFiles()

