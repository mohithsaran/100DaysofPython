# Strings are immutable
a = "!!!! Mohith !!!!"
print(len(a))
print(a.upper())
print(a)  # since immutable so it will not change the original value
print(a.lower())
print(a.rstrip('!'))  # removes the trailing characters
print(a.lstrip('!'))  # removes the leading characters
print(a.replace("Mohith", "Harry"))
print(a.split(" "))  # ['!!!!', 'Mohith', '!!!!']
print(a.split("!"))  # ['', '', '', '', ' Mohith ', '', '', '', '']
blogHeading = "introduction to pyThoN"
print(blogHeading.capitalize())  # Introduction to python
str1 = "Welcome to the console!!"
print(len(str1))  # 24
print(str1.center(60))  # Welcome to the console!!
print(len(str1.center(60)))  # 60

print(str1.endswith("!!"))  # true
str1 = "Welcome to the console!!"
print(str1.endswith("to t", 5, 12))  # true
print(str1.endswith("to", 5, 12))  # false
print(str1.startswith("W"))
print(str1.find('the'))  # 11
print(str1.find('man'))  # -1
print(str1.index('the'))  # 11
# print(str1.index('man')) #valueError
str1 = "HiMohith"
print(str1.isalnum())  # true
print(str1.isalpha())  # true
print(str1.islower())  # false
print(str1.isupper())  # false
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())  # true
str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())  # false

str1 = "        "  # using Spacebar
print(str1.isspace())  # true
str2 = "My name      "  # using Tab
print(str2.isspace())  # false

str1 = "World Health Organization"
print(str1.istitle())  # returns true if the first letter of each word is capital so true
str2 = "world health organisation"
print(str2.title())  # World Health Organization

print(str2.swapcase())
str1 = "Python is a Interpreted Language"
print(str1.swapcase())









