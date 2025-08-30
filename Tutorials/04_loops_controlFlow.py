""" ---- LOOPS ----
Demonstrates:
  - for loops with range() and iteration over sequences
  - while loops
  - Emulating do-while loops in Python
  - break and continue statements
  - Loop else clause
"""

""" --- 1) FOR Loops ---
# start: The starting number of the sequence (inclusive).
# stop: The ending number of the sequence (exclusive).
# step: The difference between each number in the sequence.
"""

print("Practicing some loops..")

for rand_letter in range(5): #same as range(0,5) 0 to 5
    print(rand_letter)
# for iterator in range(2,6):
#     print(iterator)
# for i in range(1,10,2):
#     print(i)
name = "George"
# for i in name:
#     print(i)
#     print(i, end=",")

fruits = ["apple", "banana", "mango", "watermelon"]
# for fruit in fruits:
#     print(fruit)
#     # print(fruit, end=",")
#     for char in fruit:
#         print(char)
#        # print(char, end=",")

# ran = int(input("Enter total numbers to be entered: "))
# for i in range(ran):
#     nums = int(input("Enter: "))
#     print(nums)

""" 2) --- WHILE Loops --- """

# initial = 0
# while(initial<7):
#     print(initial)
#     initial += 1

# user_input = int(input("Enter number: "))
# print(user_input)
# while(user_input < 30):
#     user_input = int(input("Enter number: "))
#     print(user_input)
# else: 
#     print("Sorry the limit was till 30 only")

""" 3) --- DO WHILE Loops --- 
Python doesn't have a built-in do-while, but this pattern runs the loop at least once.
"""

# while True:
#   number = int(input("Enter a positive number: "))
#   print(number)
#   if not number > 0:
#     break

""" 4) --- BREAK & CONTINUE ---
Break --> Comes out of the Loop
Continue --> Comes out of the iteration
"""

# for x in range(1,11):
#     if(x%3==0):
#         print("Ohh stop divisible by 3 ")
#         break
#     print("5 x ", x, "=", 5*x)

# for x in range(1,11):
#     print("5 x ", x, "=", 5*x)
#     if(x%3==0):
#         print("Ohh stop divisible by 3 ")
#         break

# for x in range(1,11):
#     if(x%3==0):
#         print("Ohh leave this is divisible by 3 also")
#         continue
#     print("5 x ", x, "=", 5*x)

# for x in range(1,11):
#     print("5 x ", x, "=", 5*x)
#     if(x%3==0):
#         print("Ohh leave this is divisible by 3 also")
#         continue

""" --- LOOPS with ELSE ---
Else part prints only when the loop is successfully ended.
if the loop is broken in between the else part will not run.
"""
# for i in range(5):
#     print(i)
# else:
#     print("Loop ended")

# for o in range(6):
#     print(o)
#     if(o==3):
#         break
# else:
#     print("Loop broken")