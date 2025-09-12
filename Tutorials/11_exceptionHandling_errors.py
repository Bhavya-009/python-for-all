""" ---- EXCEPTION HANDLING & ERRORS ----
Exceptions:
  - Exceptions are errors detected during program execution.
  - They disrupt the normal flow of a program unless handled.
  - Common built-in exceptions:
      * ZeroDivisionError → division by zero
      * ValueError        → invalid value for operation
      * IndexError        → invalid index for a sequence
      * KeyError          → missing key in a dictionary
      * TypeError         → operation applied to an inappropriate type
      * FileNotFoundError → file or directory not found
      * AttributeError    → invalid attribute reference
      * ImportError       → import failure

Keywords & Their Purpose:
  try       → Defines a block of code to test for errors.
  except    → Defines a block of code to run if an error occurs.
  else      → Defines a block to run if no errors occur in try block.
  finally   → Defines a block to run no matter what (error or not).
  raise     → Triggers a specific exception manually.

Best Practices:
  - Always catch specific exceptions (e.g., `except ValueError:`) instead of using bare `except:`.
  - Use `finally` for cleanup actions (e.g., closing files, releasing resources).
  - Avoid swallowing exceptions silently; log them or re-raise if needed.
  - Use `assert` for debugging checks, not for production input validation.
  - Group related exception handling logic together for clarity.

Advanced Notes:
  - You can chain exceptions with `raise NewError(...) from original_error`.
  - Custom exceptions can be created by subclassing `Exception`.

"""


# user_input = input("Enter the number: ")
# print(f"Multiplication table of {user_input} is: ")
# try:
#   for i in range(1, 11):
#     print(f"{int(user_input)} X {i} = {int(user_input)*i}")
# except:
#   print("Invalid Input!")
# print("Some imp lines of code")
# print("End of program")

# try:
#     num = int(input("Enter an index no. to access the list: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
# except IndexError:
#   print("Index Error")

# -- FINALLY KEYWORD --

# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer.")
# else:
#     print("Integer Accepted.")
# finally:
#     print("This block is always executed.")

def func1():
  try:
    num_list = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(num_list[i])
    return "done"
  except:
    print("Some error occurred")
    return "err"

  finally:
    print("I am always executed")
  # print("I am always executed")
 
print(func1())

# try:
#     num1 = int(input("Enter first no. "))
#     num2 = int(input("Enter second no. "))
#     ans = (num1/num2)
#     print(f"Division of {num1} and {num2} is: {ans:.2f}")
# except ZeroDivisionError:
#     print("Not defined")
# finally:
#     print("Calculation completed")

                                    #  ---- CUSTOM ERRORS ----

# age = int(input("Enter your age: "))
# if(age > 100 or age < 1):
#     raise ValueError("Enter valid age.")
# else:
#     print("Welcome")