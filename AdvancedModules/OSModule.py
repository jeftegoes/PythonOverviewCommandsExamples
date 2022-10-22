import os
import shutil

import send2trash

f = open("practice.txt", "w+")
f.write("This is a test string.")
f.close()

print(os.getcwd())
print(os.listdir())
print(os.listdir("C:\\users\\jefte"))
# shutil.move("practice.txt", "C:\\users\\jefte")
send2trash.send2trash("practice.txt")

for folder, sub_folders, files in os.walk("ExampleTopLevelFolder"):
    print(f"Currerntly looking at {folder}")
    print("\n")
    print("The subfolders are: ")
    for sub_fold in sub_folders:
        print(f"Subfolder: {sub_folders}")
    print("\n")
    print("The files are: ")
    for f in files:
        print(f"File: {f}")
    print("\n")
