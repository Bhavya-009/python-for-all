""" ---- TUPLES ----
# Same as list just a single difference is that it can not be updated (instead a new tuple is formed)
"""
my_tuple1 = (1,6,8,9,0,8)
print(my_tuple1, type(my_tuple1), len(my_tuple1))

my_tuple2 = (89)
# Without a comma, this is an int, not a tuple.
# print(my_tuple2, type(my_tuple2)) # Output : 89 int 
my_tuple2 = (89,)
# print(my_tuple2, type(my_tuple2)) # Output : 89 tuple

# Same slicing, indexing, finding the presence --
my_tuple3 = my_tuple1.count(8)
# print(my_tuple3)
# tuple.index(element, start, end)
my_tuple4 = my_tuple1.index(8,0,3) # first occurrence
# print(my_tuple4)

# --- PRESENCE CHECKS IN TUPLES ---
my_tuple5 = (10, 20, 30, 40)

# Check if a value exists in the tuple
# print(20 in my_tuple5)       # True
# print(50 in my_tuple5)       # False

# Check if a value does NOT exist in the tuple
# print(20 not in my_tuple5)   # False
# print(50 not in my_tuple5)   # True


"""
Tuples are immutable, hence if you want to add, remove or change tuple items, 
then first you must convert the tuple to a list. 
Then perform operation on that list and convert it back to tuple.
"""

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
# temp.append("Russia")         #add item (russia in the last place)
# temp.pop(3)                 #remove item (remove england)
# temp[2] = "Finland"         #change item (replace india to finland)
# countries = tuple(temp)
# print(countries)

# directly concatenate two tuples without converting them to list.
# countries = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)