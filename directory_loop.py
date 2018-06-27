#Prints names of all files and folder in directory entered

import os
path = input('Please enter the file path with two backslahses separating directories:\n')
cur_dir = os.listdir(path)
print(path)

def nav_subdir(cur_path, path_spacing):
    new_dir = os.listdir(cur_path)
    path_spacing = path_spacing + "      " 
    for file_name2 in new_dir:
        path_len = len(cur_path)
        cur_path = cur_path + "\\" + file_name2
        if os.path.isfile(cur_path):
            print(path_spacing + file_name2)
            trim_len = len(cur_path) - path_len
            cur_path = cur_path[:-trim_len]
        else:
            print(path_spacing + "-" + file_name2)
            nav_subdir(cur_path, path_spacing)
            trim_len = len(cur_path) - path_len
            cur_path = cur_path[:-trim_len]

for file_name in cur_dir:
    path_spacing = ""
    cur_path = path + "\\" + file_name
    if os.path.isfile(cur_path):
        print(file_name)
    else:
        print("-" + file_name)
        nav_subdir(cur_path, path_spacing)