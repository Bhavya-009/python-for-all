""" --- IMPORT --- """
""" 1)  BUILT-IN FUNCTIONS IMPORT """

import math
print(dir(math)) # Shows all the funcs within math 

# a = math.sqrt(3) * math.pi
# print(a)

# import math as m
# print(m.sqrt(6))

# from math import sqrt, pi
# print(sqrt(4)*pi)

# from math import sqrt as s, pi as p, floor as f
# print(f(s(25)*p))

""" 2) USER DEFINED FUNCTIONS IMPORT """
# import sample_function as sf
# print(sf.funcGreat(3,3))

# from sample_function import factorial
# print(factorial(5))


"""  3) OS MODULE
    "1. Working with Directories": 
- os.getcwd() → Get current working directory
- os.chdir(path) → Change current directory
- os.listdir(path) → List files in directory
- os.mkdir(path) → Create a new directory
- os.makedirs(path) → Create nested directories
- os.rmdir(path) → Remove empty directory
- os.removedirs(path) → Remove directories recursively

    "2. File Operations": 
- os.rename(src, dst) → Rename file or directory
- os.remove(path) → Delete a file

    "3. Path Operations (os.path)": 
- os.path.exists(path) → Check if path exists
- os.path.isfile(path) → Check if path is a file
- os.path.isdir(path) → Check if path is a directory
- os.path.abspath(path) → Get absolute path
- os.path.join(path1, path2) → Join paths safely

    "4. Environment Variables": 
- os.getenv('VAR') → Get environment variable
- os.environ['VAR'] = value → Set environment variable

    "5. Running System Commands":
- os.system('command') → Run shell command (use subprocess for advanced)

    "6. System Info": 
- os.name → OS type ('posix', 'nt', etc.)
- platform.system() → Platform name ('Windows', 'Linux', etc.)

    "7. Directory Tree Traversal":
- os.walk(path) → Iterate through directory tree
  for root, dirs, files in os.walk('folder'):
      print(root, dirs, files)
"""

import os
print(dir(os))
print("Current Directory: ", os.getcwd())
# OS TYPE ---
print("OS Type: ", os.name)

# os.mkdir("Trial Folder")

# --- CHECK IF PATH EXISTS ---
# print("Does path exist?", os.path.exists("folder"))

# --- SPLIT PATH ---
# print("Split Path:", os.path.split("/usr/bin/python"))

# CREATING ---
# for i in range (10):
    # os.mkdir("tut5")

# REMOVING ---
# for i in range (6,11):
#     os.rmdir(f"tut{i}")

# RENAME / MOVING ---
# for i in range (1, 6):
#     os.rename(f"tut{i}", f"tutorial {i}")

# Make folder only if NOT exists ---
# os.makedirs("folder", exist_ok=True)

# Making nested FOLDERS ---
# nested_path = "\\parent_folder\\child_folder\\grandchild_folder"
# os.makedirs(nested_path, exist_ok=True)
# print(f"Nested folders created at: {nested_path}")

# Making file under a folder ---
# os.mkdir("Trial Folder\\tutorial 3\\mynotes")

# Listing files under any folder ---
# myfolder = os.listdir("Trial Folder")
# print(myfolder)
# for folders in myfolder: 
#     print(folders)
#     print(os.listdir(f"Trial folder\\{folders}"))

# Join the folder and filename into a full path ---
# folder = "Trial Folder\\tutorial 1"
# file = "random.txt"
# full_path = os.path.join(folder,file)
# print("Full path: ", full_path)
