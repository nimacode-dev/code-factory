# CHECK LINE 30 >>> for introduction of app

import os
import glob

# select all files in folder which sorter.py exist
files_list = glob.glob('*')

# creat set for collecting extentions of files
extentions_set = set()

# adding extention names in extention_set
for each_file in files_list:
    extention = each_file.split('.')[1]
    extentions_set.add(extention)

# crear folders/directories
def creat_folder():
    for each_extention in extentions_set:
        os.makedirs(each_extention + '_files')

# moving files to folders we created
def move_files():
    for each_file in files_list:
        extention = each_file.split('.')[1]
        # '/'+ nameOfFile must be in end of rename to move file
        os.rename(each_file, extention+'_files/'+each_file)


# introducing app
print("NP1-FileSorter V1.0 running...\n")
print("sorting files by thier extentions")
print("creating folders and moving files in them")
print("for example : ")
print("music.mp3 is file")
print("mp3_files is folder and it was created because music.mp3 extention is mp3")
print("music.mp3 moved to mp3_files")

# runing functions
creat_folder()
move_files()
