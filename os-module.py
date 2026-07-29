import os

file = input("Enter the filename:")

if os.path.exists(file):
    os.remove(file)
    print("File Deleted Successfully")
else:
    print("File Not Found")



os.mkdir("SecurityReports")

print("Folder Created Successfully")

file_name = input("Enter the filename:")



if os.path.exists(file_name):
    print("File Found")
else:
    print("FileNotFound")

file_list = os.listdir()

print("Files in current directory:")



for file in file_list:
    print(file)

file_list = os.listdir()

print("Files in Current Directory:")
print(file_list)



location = os.getcwd()

print("Current Working Directory", {location})