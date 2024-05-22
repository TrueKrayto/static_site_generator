from textnode import TextNode
import os, shutil

def copy_static(path, dest):
    files = os.listdir(path)
    for file in files:
        new_path = path + "/" + file
        if os.path.isfile(new_path):
            shutil.copy(new_path, dest)
        else:
            new_dest = dest + "/" + file
            new_path = path + "/" + file
            os.mkdir(new_dest)
            copy_static(new_path, new_dest)

def main():
    absolute_path = os.path.abspath(__file__)
    directory = os.path.dirname(absolute_path)
    parent_dir = os.path.dirname(directory)
    path = parent_dir + "/public"
    shutil.rmtree(path, ignore_errors=True)
    if not os.path.exists(path):
        os.mkdir(path)
    data_path = directory + "/static"
    copy_static(data_path, path)
    
main()