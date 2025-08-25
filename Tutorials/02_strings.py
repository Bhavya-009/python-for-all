"""  ---- STRINGS  ----

Strings are IMMUTABLE → once created, they cannot be changed in place.  
String variables can be reassigned to a new string.

Common String Methods in Python:

1  -- upper()            → Returns a copy of the string with all characters in uppercase.  
2  -- lower()            → Returns a copy of the string with all characters in lowercase.  
3  -- strip(chars)       → Removes leading and trailing characters (default: spaces).  
4  -- lstrip(chars)      → Removes leading characters (default: spaces) from the left end.  
5  -- rstrip(chars)      → Removes trailing characters (default: spaces) from the right end.  
6  -- replace(a, b)      → Replaces all occurrences of substring 'a' with 'b'.  
7  -- split(sep)         → Splits the string into a list using the given separator.  
8  -- rsplit(sep)        → Splits the string from the right into a list.  
9  -- splitlines()       → Splits the string at line breaks into a list.  
10 -- join(iterable)     → Joins elements of an iterable into a single string using the current string as a separator.  
11 -- capitalize()       → Capitalizes the first character, makes the rest lowercase.  
12 -- casefold()         → Aggressively converts string to lowercase for case-insensitive comparisons.  
13 -- center(width, fillchar) → Centers the string in a field of given width, padded with fillchar.  
14 -- count(sub)         → Counts occurrences of substring 'sub' in the string.  
15 -- endswith(suffix)   → Checks if the string ends with the given suffix (returns bool).  
16 -- startswith(prefix) → Checks if the string starts with the given prefix (returns bool).  
17 -- find(sub)          → Returns the lowest index of substring 'sub', or -1 if not found.  
18 -- rfind(sub)         → Returns the highest index of substring 'sub', or -1 if not found.  
19 -- index(sub)         → Returns the lowest index of substring 'sub', raises ValueError if not found.  
20 -- rindex(sub)        → Returns the highest index of substring 'sub', raises ValueError if not found.  
21 -- isalnum()          → Returns True if string contains only letters and numbers (no spaces).  
22 -- isalpha()          → Returns True if string contains only letters (no digits or spaces).  
23 -- isascii()          → Returns True if all characters are ASCII.  
24 -- isdecimal()        → Returns True if all characters are decimal digits.  
25 -- isdigit()          → Returns True if all characters are digits.  
26 -- isnumeric()        → Returns True if all characters are numeric values.  
27 -- islower()          → Returns True if all alphabetic characters are lowercase.  
28 -- isupper()          → Returns True if all alphabetic characters are uppercase.  
29 -- isprintable()      → Returns True if all characters are printable (no escape sequences).  
30 -- isspace()          → Returns True if the string contains only whitespace characters.  
31 -- istitle()          → Returns True if each word starts with an uppercase letter followed by lowercase letters.  
32 -- swapcase()         → Swaps the case of each character (upper ↔ lower).  
33 -- title()            → Returns the string in title case (first letter of each word capitalized).  
34 -- zfill(width)       → Pads the string on the left with zeros until it reaches the given width.  
35 -- format(...)        → Formats a string using placeholders and values.  
36 -- format_map(mapping) → Formats a string using dictionary keys and values.  
37 -- encode(encoding)   → Returns the encoded version of the string (default: UTF-8).  
38 -- expandtabs(tabsize) → Replaces tab characters with spaces.  

import string : 
| Constant                 | Description                                                         | Example Output                                           |        |
| ------------------------ | ------------------------------------------------------------------- | -------------------------------------------------------- | ------ |
| `string.ascii_lowercase` | All lowercase letters                                               | `"abcdefghijklmnopqrstuvwxyz"`                           |        |
| `string.ascii_uppercase` | All uppercase letters                                               | `"ABCDEFGHIJKLMNOPQRSTUVWXYZ"`                           |        |
| `string.ascii_letters`   | All letters (upper + lower)                                         | `"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"` |        |
| `string.digits`          | All digit characters                                                | `"0123456789"`                                           |        |
| `string.punctuation`     | All special characters                                              | `"!"#$%&'()*+,-./:;<=>?@[\]^_`{                          | }\~"\` |
| `string.whitespace`      | Space, tab, newline, etc.                                           | `" \t\n\r\x0b\x0c"`                                      |        |
| `string.printable`       | All printable characters (letters, digits, punctuation, whitespace) | Combination of above                                     |        |


"""

# TEST :
if __name__ == "__main__":
    print("Python Strings script loaded successfully!")

# error_words = "multiple 
# lines cannot be written in python
# "  -- error

sample_words = """ Here i can
write multiple lines 
without error
"""
print(sample_words)

# To print all characters in word string :
# for character in sample_words:
#     print(character)


# ---- 1) SLICING ----
fruit = "Watermelon"
print(fruit)
print(len(fruit))

# print(fruit[0:5]) # Including 0 and not 5
# print(fruit[:5]) # same as [0:5]

# print(fruit[5:10]) # same as [5:10]
# print(fruit[5:]) # same as [5:length of string] that is [5:10]

# print(fruit[1:6]) # Including 1 and not 6

# Negative Slicing
# print(fruit[:len(fruit)-5])
# print(fruit[:-5]) # same as [0:length of fruit - 5]

# print(fruit[-6:-4]) # same as [length - 6 : length - 4] that is 10-6 : 10-4 = 4:6

# ---- 1_a) REVERSING STRINGS ----
greet_boys = "Hello Boys"
# print(greet_boys)
# print(greet_boys[::-1])


# ---- 2) OPERATIONS ON STRINGS ----
# Strings are immutable in Python → methods return a new string instead of modifying the original
# Creates word duplicate of the original, so the original remains the same and cannot be edited

lower_word = "brain"
# print(lower_word.upper())
# print(lower_word) #did not change

capital_word = "CUPTAN"
# print(capital_word.lower())

sample_word = "  space space  "
# print(sample_word.strip()) # remove space only before and after the text and not from between

greet = " helo !!!"
# print(greet.rstrip("!")) #removes the specified characters

greet_spanish = " hola "
# print(greet_spanish.replace("a","o")) # replace every character

sample_num = " First Second Third "
modify_num = sample_num.split(" ")
# print(type(sample_num))
# print((modify_num)) # splits into list from spaces
# print(type(modify_num))

sample_num1 = "first second third first last first"
# print(sample_num1.split("first"))
# print(sample_num1.split(" first ")) #caution - spaces affects the outputs

irregular_word = "capaTiaL"
# print(irregular_word.capitalize()) #capitalizes the first character

main_line = "welcome to the New world"
# print(main_line.title()) #capitalize first letter of every word

add_word = "new world"
# print(add_word.center(15, ".")) #gives space from starting and can also fill that space

sample_alpha = "abcdefgABCDEFGabcdefg"
# print(sample_alpha.count("a")) # counts the total no of occurrence

greet_friend = "Hello my friend, my friend"
# print(greet_friend.find("my friend")) # finds the first occurrence
# print(greet_friend.find("My friend")) # if not found it will return -1

greet_jupyter = "hello jupyter"
# print(greet_jupyter.index("jupyter"))
# print(greet_jupyter.index("Jupyter")) # if not found throws ERROR


# ---- 3) Boolean results ----
express = "thank you !"
# print(express.endswith("you!"))
# print(express.endswith("you !")) # spaces matters in the output
# print(express.endswith("you"))
# print(express.startswith("thank"))

express_1 = "Welcomeguys1"
# print(express_1.isalnum()) #returns true when only alphabets and numbers are present--returns false even if word space is in the string
express_2 = "welcome guys2"
# print(express_2.isalnum())
express_3 = "thanks"
# print(express_3.isalpha()) # returns true only if only alphebets are present
express_4 = "thanks6" 
# print(express_4.isalpha())

number = "231"
# print(number.isnumeric()) # returns true only if only numbers are present
number_1 = "231lol"
# print(number_1.isnumeric())

rand_word = "case"
# print(rand_word.islower()) # returns true if the letter are lower 
rand_word_1 = "CASE"
# print(rand_word_1.isupper()) # returns true if the letter are upper 
rand_word_2 = "CASe"
# print(rand_word_1.islower())
# print(rand_word_1.isupper())
rand_word_3 = "  myname\thaha  "
# print(rand_word_2)
# print(rand_word_2.isprintable()) # returns true if no escape sequence is present
# print(rand_word_2.isspace()) # checks if string has only space
# print(rand_word_2.istitle()) # every first letter of the word should be capital
rand_word_4 = "  "
# print(rand_word_4.isspace())
rand_word_5 = " heLLo friEnds "
# print(rand_word_5)
# print(rand_word_5.swapcase()) #replace capital to small n vice versa

# x = "Myname"
# if "My" in x:
#     print("yes")
# else:
#     print(0)


