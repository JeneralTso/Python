'''
Jenny Tso
Python Shutil Module Drill

'''

from shutil import copy
from os import listdir, path, remove

src_FolderA = "C:\Users\Student\Desktop\Folder A"
dst_FolderB = "C:\Users\Student\Desktop\Folder B"

def copyDeleteFiles():
    src_files = listdir(src_FolderA)
    for files in src_files:
        origFile = path.join(src_FolderA, files)
        if path.isfile(origFile):
            copy(origFile, dst_FolderB)
            remove(origFile)

def listCopiedFiles():
    dst_files = listdir(dst_FolderB)
    for copiedFiles in dst_files:
        eachCopiedFile = path.join(dst_FolderB, copiedFiles)
        print eachCopiedFile

print "The following files were successfully moved: \n"
copyDeleteFiles()
listCopiedFiles()
