""" Modes in File Handling
Mode	    Description
"r"	    Read (default mode)
"w"	    Write (creates or overwrites)
"a"	    Append (adds to the end)
'x'	    Create (error if file exists)
'b'	    Binary mode
't'	    Text mode (default)
You can combine modes: "rb", "wt", etc.
"""
""" DIFFERENCE between read() and readlines() ---->
 read(): Reads the Entire File as a Single String
 readlines(): Reads the File into a List of Lines

| Feature        | `read()`                          | `readlines()`                        |
| -------------- | --------------------------------- | ------------------------------------ |
| Returns        | Single string                     | List of strings                      |
| Structure      | Whole file in one string          | One string per line                  |
| Includes `\n`? | Yes                               | Yes (at end of each line)            |
| Best for       | Processing entire content at once | Line-by-line processing (with index) |

--> Example Use Cases :
Use read() when:
You want the whole text and will process it as a single string (e.g., word count, searching substrings).

Use readlines() when:
You want to loop or process specific lines (e.g., skip headers, line-by-line analysis).

"""

# --- READING FILES ---
file_r = open("text.txt", "r")
print(file_r)
read = file_r.read()
print(read)
# Read line by line ---
# with open("text.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# --- WRITING FILES ---
file_w = open("text.txt", "w")
# file_w.write("\n This text is written through python code! ") # deletes the text already present
# file_w.close()

# --- APPENDING FILES ---
file_a = open("text.txt", "a")
# file_a.write("\n This is added by appending")
# file_a.close()


# with KEYWORD --- for closing a file automatically
# with open("text.txt", "r") as t:
#     print(t.read())

# --- CREATING FILES SAFELY ---
import os
# if(os.path.exists("new.txt") == False):
#     new_file = open("new.txt", "x")
#     new_file.close()

# with open("new.txt", "a") as n:
#     n.write("\n Hello newly created file")

# try:
#     with open("new.txt", "r") as n:
#         print(n.read())
# except:
#     print("File does not exists")

# --- WRITING MULTIPLE LINES ---
# lines_list = ["\nline1", "\nline2", "\nline3"] # can also be used 
# lines = []
# for i in range(1,11):
#     l = f"\nLINE {i}"
#     lines.append(l)
# print(lines)
# with open("text.txt", "a") as f:
#     # f.write(lines) -- TypeError: write() argument must be str, not list
#     f.writelines(lines)

# --- BINARY FILE READING ---
# try :
#     with open("image.png", "rb") as file:
#         print(file.read())
# except FileNotFoundError: 
#     print("File not found")

# --- FILE PATH OPERATIONS ---
# import os
# file_path = os.path.join("folder", "example.txt")

# Check if a file exists
# if os.path.exists(file_path):
#     print("File exists.")
# else:
#     print("File not found.")

# readlines() ---
# with open("new.txt", "r") as n:
#     file_read = n.read()
#     print(file_read)

# with open("new.txt", "r") as n:
#     file_readlines = n.readlines()
#     print(file_readlines)

# --- READING MARKS EXAMPLE ---
# f = open("mark.txt", "r")
# i = 0
# while True:
#     i += 1
#     line = f.readline()
#     if not line:
#         break
#     p = int(line.split(",")[0])
#     c = int(line.split(",")[1])
#     m = int(line.split(",")[2])
#     print(f"Marks of student {i} in Physics is : {p}")
#     print(f"Marks of student {i} in Chemistry is : {c}")
#     print(f"Marks of student {i} in Maths is : {m}")
#     print(line)

# --- FILE POINTER METHODS (seek, tell, truncate) ---
# seek(), tell(), truncate()
# with open("random.txt", "r") as random:
#     # starts reading from 5 bytes further
#     random.seek(5) 
#     # prints from where the reading is seeked
#     print(random.tell()) 
#     print(random.read())

# with open("random.txt", "w") as write:
#     write.write("Here is additional text")
#     prints only specified amount of bytes
#     write.truncate(10) 
# with open("random.txt", "r") as write:
#     print(write.read())
