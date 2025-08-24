#Conditional Statements

#Example Below of simple conditional statement
my_int = 4

#Indentation required for statements inside of conditionals
# 1. The `if` block:
#    - This is the starting point of the decision-making structure.
#    - You can only have ONE `if` block in an if-elif-else structure.
#    - It checks a condition (in this case, if `my_int == 5`).
#    - If the condition is True, the code inside the `if` block executes.
if my_int == 5:
    print('my_int equals 5')
# 2. The `elif` block:
#    - Stands for "else if".
#    - You can have MULTIPLE `elif` blocks to check additional conditions.
#    - Each `elif` block is checked in order, only if the previous `if` or `elif` conditions are False.
#    - If the condition in the `elif` block is True, the code inside it runs, and no further blocks are checked.
elif my_int == 4:
    print('my_int equals 4')
# 3. The `else` block:
#    - The `else` block is optional and can be used at most ONCE.
#    - It executes only if NONE of the `if` or `elif` conditions are True.
#    - The `else` block does not check a condition—it runs as a default case.
else:
    print('my_int does nto equal 4 or 5')

#--------------------------------------------------------------------------------#

#Coding Exercise #19 - Grader

student_score = 75

# Write your if block here:
if student_score >=90:
    grade = "A"
elif student_score >=80:
    grade = "B"
elif student_score >=70:
    grade = "B"
elif student_score >=60:
    grade = "B"
else:
    grade = "F"

print('The grade is:', grade)

#--------------------------------------------------------------------------------#
# Truthiness in Python: Basics
# In Python, conditions in if-statements evaluate to boolean values: True or False.

# Example of a boolean condition
if 5 == 5:
    print('The condition is True')  # This will print
    print(type(5 == 5))  # Outputs: <class 'bool'>

# Truthy and Falsy Values
# Python considers certain values as "Truthy" or "Falsy".
# Truthy values are treated as True, and Falsy values are treated as False.

# Examples of Truthy and Falsy Values

# Numeric Values
if 5:  # Non-zero numbers are Truthy
    print('5 is Truthy')

if -5:  # Negative numbers are also Truthy
    print('-5 is Truthy')

if 0:  # Zero is Falsy
    print('0 is Truthy')  # This will not print

# Strings
if "Hello":  # Non-empty strings are Truthy
    print('"Hello" is Truthy')

if "":  # Empty strings are Falsy
    print('Empty string is Truthy')  # This will not print

if "   ":  # Strings with spaces are also Truthy
    print('String with spaces is Truthy')

# Variables
my_var = 5
if my_var:  # Any non-zero or non-empty variable is Truthy
    print(f'{my_var} is Truthy')  # Outputs: 5 is Truthy

my_var = 0
if my_var:  # Zero is Falsy
    print(f'{my_var} is Truthy')  # This will not print

my_var = ""
if my_var:  # Empty strings are Falsy
    print(f'{my_var} is Truthy')  # This will not print

my_var = None
if my_var:  # None is Falsy
    print('None is Truthy')  # This will not print

my_var = False
if my_var:  # The value False is Falsy
    print('False is Truthy')  # This will not print

# Summary of Falsy Values
# Python considers the following values as Falsy:
# - None
# - False
# - 0 (integer)
# - 0.0 (float)
# - "" (empty string)
# - [] (empty list)
# - {} (empty dictionary)
# - set() (empty set)

# Everything else is considered Truthy.
