""" ---- FUNCTIONS & RECURSION ----
Covers:
  - Built-in functions (min, max, len, sum, type, etc.)
  - User-defined functions
  - pass keyword (writing function later without syntax error)
  - Types of arguments:
      * Required arguments
      * Default arguments
      * Keyword arguments
      * Variable-length arguments (*args, **kwargs)
  - return statement (returning values from a function)
  - Recursion:
      * Concept and example (factorial function)
      * Importance of base case to prevent infinite recursion
  - Lambda (anonymous) functions

Key Notes:
  - Functions help organize code into reusable blocks.
  - *args → passes any number of positional arguments, stored as a tuple.
  - **kwargs → passes any number of keyword arguments, stored as a dictionary.
  - *args and **kwargs can be combined in a function; *args must appear before **kwargs in the parameter list.
  - Lambda functions are single-line anonymous functions, useful for small tasks where defining a full function is unnecessary.
"""



def funcLower(a,b):
    pass

def funcGreat(a,b):
    if(a>b):
        print(a,">",b)
    elif(a<b):
        print(a,"<",b)
    else:
        print(a,"=",b)
        print("wow equal!")

# input_num_1 = int(input("Enter first number: "))
# input_num_2 = int(input("Enter second number: "))
# funcGreat(input_num_1,input_num_2)

""" -- ARGUMENTS --
 - Required Arguments
 - Default Arguments
 - Keyword Arguments
 - Variable length Arguments
"""

# --- Required Arguments ---
def fullName(fname,mname,lname):
    print("Hola", fname, mname, lname)
fullName("steve","david","brown")

# --- Default Arguments ---
def full_name_default(fname,mname="David",lname="Brown"):
    print("Hola", fname, mname, lname)
# full_name_default("Steve")
# full_name_default("Steve", "Rick")

# --- Keyword Arguments ---
def full_name(fname,mname="David",lname="Brown"):
    print("Hola", fname, mname, lname)
# full_name(lname="Richardson", fname="Newey")

# * -- creates a tuple
# ** -- creates a dictionary

# --- *args (Non-Keyword Variable-Length Arguments)---
def greet_people(*names):
    for name in names:
        print("Hello,", name)
# greet_people("Alice", "Bob", "Charlie")

def name(*name):
    print("Hello,", name[0], name[1], name[2])
# name("Alice", "Richard", "Stokes")

# --- **kwargs (Keyword Variable-Length Arguments) ---
def person_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
# person_info(name="John", age=25, city="New York")

def my_name(**my_name):
    print("Hello,", my_name["fname"], my_name["mname"], my_name["lname"])
# my_name(mname = "Buchanan", lname = "Barnes", fname = "James")

def mix_example(a, *args, **kwargs):
    print("a:", a)
    print("args:", args)
    print("kwargs:", kwargs)
# mix_example(1, 2, 3, x=4, y=5)


# The return statement is used to return the value of the expression back to the calling function.
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
# print(name("James", "Buchanan", "Barnes"))


def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum += i
#   print("Average is: ", sum / len(numbers))
#   return 7
  return sum / len(numbers)

# num_list = average(5, 6, 17, 1)
# print(num_list)

""" ---- RECURSION ----
Recursion is the process of defining something in terms of itself.
"""

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
# num = int(input("Enter a number: "))
# print("The factorial of", num, "is:",factorial(num))

""" ---- Lambda Func ---- 
Used as anonymous func without name (optional) and without using "def" keyword
Syntax : lambda arguments: expression   
"""

def power_fourth(arg1, arg2):
    return arg1*arg2
sqr = lambda x: x*x
# print(sqr(5))
# print(power_fourth(sqr(2),sqr(2)))
