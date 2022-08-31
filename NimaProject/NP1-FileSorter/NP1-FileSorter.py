# CHECK LINE 45 or NP1-ReadMe >>> for introduction of app

import os
import glob

# select all files in folder which sorter.py exist
files_list = glob.glob('*')

# creat set for collecting extentions of files
extentions_set = set()

# adding extention names in extention_set
for each_file in files_list:
    # use try because if . doesn't exist >>> we can't use split
    try:
        extention = each_file.split('.')[1]
        extentions_set.add(extention)
    except:
        continue

# creat folders/directories
def creat_folder():
    for each_extention in extentions_set:
        if each_extention == 'py':
            # don't creating py_files folder
            continue
        # use try because if folder exist >>> we can't create it again
        try:
            os.makedirs(each_extention + '_files')
        except:
            continue

# moving files to folders we created
def move_files():
    for each_file in files_list:
        extention = each_file.split('.')[1]
        # use try because if file was open >>> we can't move it
        try:
            # '/'+ nameOfFile must be in end of rename to move file
            os.rename(each_file, extention+'_files/'+each_file)
        except:
            continue


# introducing app
print("NP1-FileSorter V1.1 running...\n")
print("sorting files by thier extentions")
print("creating folders and moving files in them")
print("for example : ")
print("music.mp3 is file")
print("mp3_files is folder and it was created because music.mp3 extention is mp3")
print("music.mp3 moved to mp3_files")

# runing functions
creat_folder()
move_files()
