""" ---- ENUMERATE FUNCTION ----
Purpose:
  - The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
  - Useful when you need both the index and the value while looping.

Syntax:
  enumerate(iterable, start=0)

Parameters:
  iterable → Any iterable (list, tuple, string, etc.)
  start    → The starting index (default is 0)

Returns:
  - An enumerate object (iterator) that yields pairs (index, value) for each element.

Key Notes:
  - enumerate() is often used instead of manually creating a counter variable.
  - You can unpack the index and value directly in the loop: 
      for index, value in enumerate(iterable):
  - The start parameter can be set to any integer to change the starting index.

Common Use Cases:
  1) Looping with index and value without manual counter
  2) Labeling or numbering items in output
  3) Updating elements in place using index
  4) Iterating over strings with index reference
  5) Combining with zip() for working over multiple iterables

"""


fruits = ["apple", "banana", "kiwi", "mango", "orange"]
price_per_kg = [80, 30, 160, 120, 40]
fruit_code_name = ["a", "b", "k", "m", "o"]

numbers = [10, 20, 30]

# Normal iteration -
# for fruit in fruits:
#     print(fruit)

# --- BASIC USAGE ---
for index,fruit in enumerate(fruits):
    print(index,fruit)

# --- WITH MULTIPLE LISTS (zip) ---
# for index,(fruit,code, price) in enumerate(zip(fruits,fruit_code_name,price_per_kg), start=1):
#     print(index, fruit, code, price)

# --- CONVERT TO LIST ---
# list_enumerate = list(enumerate(fruits))
# print(list_enumerate)

# --- UPDATING LIST WITH ENUMERATE ---
# for i, num in enumerate(numbers):
#     numbers[i] = num * 2
# print(numbers)  # [20, 40, 60]

# --- ENUMERATE OVER STRING ---
# for i,letter in enumerate("brother", start=1):
    # print(f"Letter {i} : {letter}")