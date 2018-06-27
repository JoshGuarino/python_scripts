import os

path = "C:\\Users\\Josh\\Documents\\programs\\test"
cur_dir = os.listdir(path)
print(path)

def nav_subdir(cur_path, path_spacing):
    new_dir = os.listdir(cur_path)
    path_spacing = path_spacing + "         " 
    for file_name2 in new_dir:
        if "." not in file_name2:
            path_len = len(cur_path)
            print(path_spacing + "-" + file_name2)
            cur_path = cur_path + "\\" + file_name2
            nav_subdir(cur_path, path_spacing)
            trim_len = len(cur_path) - path_len
            cur_path = cur_path[:-trim_len]
        else:
            print(path_spacing + file_name2)
            

for file_name in cur_dir:
    path_spacing = ""
    cur_path = path + "\\" + file_name
    if "." not in file_name:
        print("-" + file_name)
        nav_subdir(cur_path, path_spacing)
    else:
        print(file_name)



    
        
