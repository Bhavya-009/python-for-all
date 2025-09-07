""" ---- DICTIONARIES ----
- Dictionaries store data as key-value pairs.
- Ordered (Python 3.7+), mutable, and do not allow duplicate keys.
- Keys must be immutable (hashable) types (e.g., strings, numbers, tuples).
- Values can be of any type and can be duplicated.

Common Methods:
  get(key, default)         → Returns value of key; returns default if key not found.
  keys()                    → Returns a view object of all keys.
  values()                  → Returns a view object of all values.
  items()                   → Returns a view object of all key-value pairs.
  update(other, **kwargs)   → Updates dictionary with key-value pairs from another dict or kwargs.
  pop(key, default)         → Removes the key and returns its value; default if key not found.
  popitem()                 → Removes and returns the last inserted key-value pair.
  clear()                   → Removes all items from the dictionary.
  copy()                    → Returns a shallow copy of the dictionary.
  setdefault(key, default)  → Returns value of key; inserts key with default value if key not found.
  fromkeys(iterable, value) → Creates a new dictionary with keys from iterable, all set to value.

Key Notes:
  - Dictionaries allow fast lookups by key.
  - Keys must be unique; assigning an existing key overwrites its value.
  - Use 'in' to check if a key exists.
"""


# --- CREATION ---
emp = {}
print(emp, type(emp))
emp1 = {"name":"Marnus", "age":25, "id":1253}
print(emp1, type(emp1))

# --- ACCESSING ELEMENTS ---
# print(emp1["name"])
# print(emp1.get("name")) # same as emp1["name"]
# print(emp1.get("salary", "Not Found"))  # Not Found
# --- .get() ---
# Safely retrieves the value for a given key
# If the key exists → returns its value
# If the key does NOT exist → returns the provided default (avoids KeyError)

# print(emp1.keys())
# print(emp1.values())
# print(emp1.items())
# print(emp1.keys)

# --- MODIFICATION ---
# emp1.update({"rate":85})
# emp1.update({"DOB":"12/9/2001"})
# print(emp1)

# emp1.clear()
# print(emp1)

# emp1.pop("age")
# print(emp1)

# emp1.popitem()
# print(emp1)

# del emp1["age"]
# print(emp1)

# del emp1
# print(emp1) # error since the entire dict is deleted

# --- COPY ---
original_dict = {"name": "Alice", "age": 25}
copied_dict = original_dict.copy()
# print("Copied Dictionary:", copied_dict)  # {'name': 'Alice', 'age': 25}

# --- SETDEFAULT ---
# If key exists → returns its value
# If key does not exist → inserts key with default value, then returns default
my_dict = {"fruit": "apple", "color": "red"}
result1 = my_dict.setdefault("fruit", "banana")
result2 = my_dict.setdefault("taste", "sweet")
# print("After setdefault:", my_dict)       # {'fruit': 'apple', 'color': 'red', 'taste': 'sweet'}
# print("Returned values:", result1, result2)  # apple sweet

# --- FROMKEYS ---
keys = ["a", "b", "c"]
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
# print("Fromkeys Dictionary:", new_dict, type(new_dict))  # {'a': 0, 'b': 0, 'c': 0}

# --- LOOPING THROUGH DICTIONARY ---
info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info.items())
# for key, value in info.items():
#   print(f"The value corresponding to the key {key} is {value}") 


# --- PRESENCE CHECKS ---
# print("name" in emp1)      # True if key exists
# print("salary" not in emp1)  # True if key does not exist
