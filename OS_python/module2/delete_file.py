import os

# os.remove("write_file.txt") 
# knowing what directory you are in
print(os.getcwd())
os.chdir("OS_python")
# print(os.getcwd())
print(os.listdir())
# os.mkdir("new_folder")