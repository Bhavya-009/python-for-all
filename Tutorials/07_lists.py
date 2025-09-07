""" ---- LISTS ----
Lists:
  - Ordered, mutable collections that allow duplicate values.
  - Elements can be of mixed data types.
  - Indexing starts at 0; negative indexing starts from -1.
  - List items are separated by commas and enclosed within square brackets [].
  - Many methods are same as we use with strings

Common List Methods:
  append(x)        → Adds an element x to the end of the list.
  sort()           → Sorts the list in ascending order (modifies original).
  pop(i)           → Removes and returns element at index i (default: last).
  reverse()        → Reverses the order of the list in place.
  insert(i, x)     → Inserts element x at index i.
  extend(iterable) → Adds elements from another iterable to the end of the list.
  copy()           → Returns a shallow copy of the list.
  count(x)         → Returns the number of occurrences of x in the list.
  index(x)         → Returns the index of the first occurrence of x.
  clear()          → Removes all items from the list.

Tuples:
  - Ordered, immutable collections that allow duplicate values.
  - Elements can be of mixed data types.
  - Once created, elements cannot be modified directly.

Common Tuple Methods:
  count(x)         → Returns the number of occurrences of x in the tuple.
  index(x)         → Returns the index of the first occurrence of x.

Key Notes:
  - Lists are mutable → can change elements after creation.
  - Tuples are immutable → to modify, convert to a list, change, then convert back.
  - Both support slicing, indexing, and `in` / `not in` checks.
"""


num_list = [1,5,6,7,8]
print(num_list, type(num_list))
mix_list = ["wow", "hello", 1, 10]
print(mix_list, type(mix_list))

""" 1) -- INDEXEING & SLICING -- """
num_list1 = [101,102,103,104,105,106,107,108]
# print(len(num_list1))
# print(num_list1[:]) # default [0:length of list]
# print(num_list1[0])
# print(num_list1[1:5]) # slicing

# -- Negative Indexing --
# print(num_list1[:-3])
# print(num_list1[1:-2]) # [1: length of list - 2]
# # listName[start : end : jumpIndex]
# print(num_list1[::]) #default [0:length:0]
# print(num_list1[::3])

""" --- SEARCHING : Presence --- """
# if 111 in num_list1:
#     print("111 Present")
# else:
#     print("111 Not present")

""" --- LIST COMPREHENSION --- 
General Form of List Comprehension : 
  [new_item for item in iterable if condition]
    new_item → what you want to put in the new list
    item → each element from the iterable (list, tuple, set, etc.)
    condition (optional) → filter elements
"""
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
# print(namesWith_O)

square = [i*i for i in range(11)]
# print(square)
even_square = [i*i for i in range(11) if i%2==0]
# print(even_square)

"""  -- LIST METHODS -- """

numbers = [5,4,8,6,4,1,0]
# print(numbers, type(numbers))
# numbers.sort()
# print(numbers)
# print(numbers.index(4))
# print(numbers.count(4)) # counts total occurrence
# numbers.append(36)
# print(numbers)
# numbers.pop(2)
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.insert(0,999)
# print(numbers)

other_numbers = [55,44,66]
# numbers.extend(other_numbers)
# print(numbers)
# other_numbers = numbers.copy() # alternative of numbers.extend
# print(other_numbers)

join_numbers = other_numbers + numbers # alternative way of concatenating
# print(join_numbers)

# --- CLEAR METHOD ---
my_list6 = [1, 2, 3, 4]
# print("Before clear:", my_list6)  # [1, 2, 3, 4]
my_list6.clear()                  # Removes all items from the list
# print("After clear:", my_list6)   # []
