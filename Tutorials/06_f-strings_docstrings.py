"""Covers:
  - f-strings: variable interpolation, expressions, formatting numbers, multi-line strings, looping with f-strings
  - docstrings: purpose, correct placement, retrieving with __doc__
"""

""" ---- F-STRINGS ---- """

# Alternative of f-string --
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Jerry"
# print(letter.format(name, country))

# Basic substitution
fname = "David"
lname = "Brown"
greet = f"Good Morning, {fname} {lname}"
print(greet)

# used if a single word is repeated alot times
val = 'Geeks'
# print(f"{val}for{val} is a portal for {val}.")  
name = 'Tushar'  
age = 23  
# print(f"Hello, My name is {name} and I'm {age} years old.")  

# Expressions inside f-strings
# print(f"{2 * 30}") #returns as string
# for i in range(6):
#     print(f"Square of {i} is {i**2}")
# for num in [1.2345, 6.789]:
#     print(f"Formatted number: {num:.2f}")
# for i in range(3):
#     print(f"""
#         Line {i+1}
#         Another line
#     """)

# Loop examples
# fnames = ["Steve", "David", "Mark"]
# for f in fnames:
#     print(f"Welcome, {f}")

first_names = ["Alice", "Bob", "Charlie"]
last_names = ["Smith", "Johnson", "Brown"]
# for first_name, last_name in zip(first_names, last_names):
#     print(f"Welcome, {first_name} {last_name}")

"""  ---- DOCSTRINGS ---- 
Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
"""

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
# square(5)
# print(square.__doc__)
# def square(n):
#     print(n**2)
#     '''Takes in a number n, returns the square of n'''
# square(5)
# print(square.__doc__) # in this case it will print none since the docstring is not written on the first line after the function starts


