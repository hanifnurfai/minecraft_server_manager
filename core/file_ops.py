import shutil
import os

#Copying a file
def copy_file(src, dst):
    shutil.copy(src, dst)

#Moving a file
def move_file(src, dst):
    shutil.move(src, dst)

#Making directory
def making_dir(name):
    os.makedirs(exist_ok=True, name=name)