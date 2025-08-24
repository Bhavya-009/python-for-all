""" 1) ---- START ---- """

# TEST :
if __name__ == "__main__":
    print("Python Basics script loaded successfully!")

# This is a single line comment

"""
Multi
Line 
Comment
"""

""" --> Writing Style
| Use Case                    | Recommended Style | Example                  |
| --------------------------- | ----------------- | ------------------------ |
| **Variables**               | `snake_case`      | `user_name = "Alice"`    |
| **Functions**               | `snake_case`      | `def calculate_total():` |
| **Classes**                 | `PascalCase`      | `class BankAccount:`     |
| **Constants**               | `UPPER_CASE`      | `MAX_USERS = 100`        |
| **Modules (file names)**    | `snake_case`      | `data_handler.py`        |
| **Packages (folder names)** | `snake_case`      | `utilities`              |
"""

print("Hello World")
print("Hey", 1, 2, sep="-", end=" statement ended and separated by - \n")
print("Learn \" Python \" ")

first_name = input("Enter your First Name : ")
last_name = input("Enter your Last Name : ")
full_name = first_name + " " + last_name
# print(" Your full name is : ", full_name)

# num1 = input("Enter your first number : ")
# num2 = input("Enter your second number : ")
# print("Addition is", num1 + num2)
# print("Addition is", int(num1) + int(num2)) #typecasting



""" 2) ---- VARIABLES ----

Everything in PYTHON IS AN OBJECT
list can store data of any datatypes and are MUTABLE (can edit)
tuple can store data of any datatypes and are IMMUTABLE (cannot edit)
dict
"""

num = 1
text = "This is a line"
decimal_num = 1.3
boolean = True
list01 = [1,2,3]
list02 = [1,2,3, "name", "surname"]
list03 = [(10,12),["apple", "banana"], ["green", "red"]]
tuple01 = (("butter", " \" bread\" ") , "cream")
tuple02 = (("cake", " \" sweet\" ") , ["cherry"]) 
#Here, tuple02 contains a list, which can be mutated even though tuples themselves are immutable
data01 = {"name":"jack", "color": "brown", "age":15}

variables = [num, text, decimal_num, boolean, list01, list02, list03, tuple01, tuple02, data01]
# for variable in variables:
#     print(variable, type(variable))


                                
""" 3) ---- OPERATORS ----

+, -, *, / ---> Basic
//  floor division (round down)
**  exponential
%   modulus

| Operator Type | Operator | Description                                    |
|---------------|----------|------------------------------------------------|
| Comparison    | ==       | Equal to                                       |
|               | !=       | Not equal to                                   |
|               | >        | Greater than                                   |
|               | <        | Less than                                      |
|               | >=       | Greater than or equal to                       |
|               | <=       | Less than or equal to                          |
| Logical       | and      | Logical AND                                    |
|               | or       | Logical OR                                     |
|               | not      | Logical NOT                                    |
| Identity      | is       | Object identity (x is y)                       |
|               | is not   | Negated object identity (x is not y)           |
| Membership    | in       | Value present in a sequence (x in y)           |
|               | not in   | Value not present in a sequence (x not in y)   |

"""

sample_number1 = 5
sample_number2 = 2
# print(sample_number1//sample_number2)
# print(sample_number1**sample_number2)
# print(sample_number1%sample_number2)

""" 4) ---- TYPECASTING ----
process of converting a variable from one data type to another. 
It can be done explicitly by the programmer using functions like int(), float(), and str(), or 
implicitly by the Python interpreter when required during operations.
"""

sample_number3 = "2.2"
sample_number4 = "6.2"
# print(sample_number3+sample_number4)

# Explicit Typecasting
# print(float(sample_number3)+float(sample_number4))

# Implicit Typecasting
# sample_number5 = 1.5 # without quotes 
# sample_number6 = 6
# print(sample_number5+sample_number6)

sample_number7 = "4"
sample_number8 = 2
# # print(sample_number7+sample_number8) - error
# print(int(sample_number7)+sample_number8)
