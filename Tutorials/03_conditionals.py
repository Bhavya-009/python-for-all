""" ---- CONDITIONALS ----
Demonstrates:
  - Comparison operators
  - Nested if-elif-else
  - Using `time` for real-world conditions
  - match-case statements (Python 3.10+)
  - Shorthand if-else

Operators: < (less than), > (greater than), <= (less than or equal), >=, == (equal), != (not equal)
"""

# TEST :
if __name__ == "__main__":
    print("Python Conditionals script loaded successfully!")

""" --- IF-ELIF-ELSE --- """

# user_num = int(input("Enter a number: "))
# print("Your number is: ", user_num)

# if(user_num < 0):
#     if(-10<=user_num<=-1):
#         print("Small negative number")
#     elif(-100<=user_num<-10):
#         print("Good negative number")
#     else:
#         print("LARGE negative number")
# elif(user_num > 0):
#     if(user_num<10):
#         print("Small positive number")
#     elif(10<=user_num<=100):
#         print("Good positive number")
#     else:
#         print("LARGE positive number")
# else:
#     print("ZERO!")

# print("conditions over!!")

""" ---- TIME ---- """

# https://docs.python.org/3/library/time.html#time.strftime
import time
print(time.ctime())

# sleep => no of seconds to skip
# for i in range(4):
#     time.sleep(1)
#     print(i)

""" Time
Index 	Attribute Name 	    Values
0	    tm_year	            0000, …, 9999
1	    tm_mon	            1, 2, …, 11, 12
2	    tm_mday	            1, 2, …, 30, 31
3	    tm_hour	            0, 1, …, 22, 23
4	    tm_min	            0, 1, …, 58, 59
5	    tm_sec	            0, 1, …, 60, 61
6	    tm_wday	            0, 1, …, 6; Sunday is 6
7	    tm_yday	            1, 2, …, 365, 366
8	    tm_isdst	        0, 1 or -1
"""


# t = time.strftime('%H:%M:%S')
# print(t)
# h = int(time.strftime('%H'))
# print(h)
# m = int(time.strftime('%M'))
# print(m)
# s = int(time.strftime('%S'))
# print(s)

# name = input("Enter your Name: ")
# if(4<=h<12):
#     print("Good Morning", name)
# elif(12<=h<16):
#     print("Good Afternoon", name)
# elif(16<=h<22):
#     print("Good Evening", name)
# else:
#     print("Good Night", name)


""" ---- MATCH CASE ----
Similar to switch case in c++
break statement is not necessary here after every case
you can use multiple default case
"""

# input_num = int(input("Enter num: "))
# print(input_num)

# match input_num:
#     case 4:
#         print("num is 4");
#     case _ if input_num!= 5:
#         print("num is not 5");
#     case _:
#         print("lol")

# print("lets decide if you can drive...")
# age = int(input("Enter your age: "))
# print("Your age is: ", age)

# match age:
#     case _ if age >= 70:
#         print("too old")
#     case _ if 18 < age < 70:
#         print("Of course!")
#     case 18:
#         print("Almost there!")
#     case 17:
#         print("Wait for a little while")
#     case _ :
#         print("no no")

""" ---- Short Hand If else Statements ---- """
# sample_num_1 = int(input("Enter any number : "))
# sample_num_2 = int(input("Enter any number again : "))
# print(sample_num_2) if sample_num_1 < sample_num_2 else print (sample_num_1) if sample_num_1 > sample_num_2 else print(sample_num_1, "=", sample_num_2)
# final_print = "great" if sample_num_1>sample_num_2 else 0
# print(final_print)

