# Ask user for their name
name = input("What is your name? ")
age = int(input("What is your age? "))
course = input("What is your course? ")

# Remove whitespaces from str
name = name.strip()

# Capitalize user's name
name = name.capitalize()

# display the name
print(f"Hello, {name}")

import sys

print(sys.version)

"""
Python 3.12.2 is installed in the machine
"""

if(sys.version_info >= (3, 12)):
    print(f"Python {sys.version_info} is installed on your local machine {name.upper()}.")

print(type(name))
print(type(sys))
print(type(sys.version_info))
print(type(3.1416))

jsonVar = {
    "Name": name.lower(),
    "Age": age,
    "Course": course.split(".")
}

print(jsonVar)

listIsJustAnArray = [1,2,3]

print(listIsJustAnArray[-1])

listIsJustAnArray.append(4)

print(listIsJustAnArray)