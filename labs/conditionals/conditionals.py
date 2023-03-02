'''
Assignment #5:

    Tests the various capabilities of the functions  
    defined in the conditionals.py file.


@author Kevin Hayden
@date 2023-02-11
@org Marist College - Department of Computing Science

Syntax for single decision:

if <condition> :
    <body>
    
Syntax for 2-way decision:

if <condition> :
    <body>
else:
    <body>

Syntax for Multi-way decision:

if <condition> :
    <body>
elif <condition> :
    <body>
else:
    <body>
    
Syntax for try/catch:

try:
    <body>
except <exception-type> :
    <body>
'''

from wsgiref import validate


def is_equilateral(x, y, z):
    if (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        if (x == y and x == z):
            return True
        else:
            return False
    else:
        raise Exception("Please enter only integers")
    
def get_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    result = []

    if (isinstance(text, str)):
        text.lower()
        for char in text:
            if char in vowels:
                result.append(char)
    else:
        raise Exception("Please enter a string")

    return result

def validate_list(grades):
    if (not isinstance(grades, list)):
        raise Exception("Grades must be in the form of a list")
    elif (grades == []):
        raise Exception("Grades must not be empty")
    elif (not all(isinstance(elem, int) for elem in grades)):
        raise Exception("Grades must contain all integers")
    elif (all(0 > elem  or elem > 100 for elem in grades)):
        raise Exception("Grades must be between 0 and 100")
    else:
        return grades

def is_palindrome(text):
    new = ""
    if (not isinstance(text, str)):
        raise Exception("Please enter a string")
    else:
        new = text[::-1]
        if (new.lower() == text.lower()):
            return True
        return False

def calculate_letter_grade(grades):
    total = 0
    avg = 0

    if (not validate_list(grades)):
        raise Exception("Invalid list")
    else:
        for i in grades:
            total += i
            avg = total/len(grades)

        if avg >= 93:
            return "A"
        elif avg >= 90:
            return "A-"
        elif avg >= 87:
            return "B+"
        elif avg >= 83:
            return "B"
        elif avg >= 80:
            return "B-"
        elif avg >= 77:
            return "C+"
        elif avg >= 73:
            return "C"
        elif avg >= 70:
            return "C-"
        elif avg >= 67:
            return "D+"
        elif avg >= 63:
            return "D"
        elif avg >= 60:
            return "D-"
        else:
            return "F"


