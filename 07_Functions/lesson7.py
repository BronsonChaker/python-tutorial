#Functions

#Below is an example of a function
#1) Use the def functions to define function
#2) name the function, this function is called my_function
#3) follow function name by parenthesis (), the inside opf the parenthesis parameters can be passed
#in to be utilised in the function body
#4) follow parenthesis by colon :
#5) indented into the function body input the code
#6) Lastly call the function where required in code
def my_function():
    print("Functions")
    print("allow you to")
    print("reuse code!")
#function call
my_function()

#---------------------------------------------------------------------#

#Parameters

#Below exmaple is a function which will add two integers together
#2 paramters passed in which will be later used in the function body
def add_two(num_1, num_2):
    sum_result = num_1 + num_2
    print(sum_result)

#function call with arguments 
add_two(5,5)

#return statement inside of function
def add_two(num_1, num_2):
    return num_1 + num_2

#assinging variable to the return value from add_two function
result = add_two(2,5)

print(result)

#setup function for power
def power(number, exponent):
    return number ** exponent

#this function is the same as above but this allows the user the option to only pass in the number
#and automarically setting the exponent so the uder can do power(4) and exponnet is already set.
#the user still has the option however to set the exponent such as power(4,3)
def power(number, exponent=2):
    return number ** exponent


# Complete the area() function here:
def area(length, width=15):
    return length * width


#-----------------------------------------------------------------#

#Coding Exercise 26: Rectangle Calculations

# Complete the perimeter() function here:
def perimeter(length, width=15):
    return 2 * (length + width)

print("Area of the rectangle:", area(20, 10))               # 200
print("Perimeter of the rectangle:", perimeter(20, 10))     # 60

print("Area using default width:", area(20))                # 300
print("Perimeter using default width:", perimeter(20))      # 70

#-----------------------------------------------------------------#

#Variable Scope

#setting a variable(global)
global_var = "I am a global variable"

#setting a function and accessing global and local variable
def my_function():
    local_var = "I am a local variable"
    print(local_var)
    print(global_var)

#calling function
my_function()

#able to print this as this is deifned outside of any functions and defiuned globally 
print(global_var)

#cannot access this local_var as it is defined in my_function body and not accesible outside of
#the function

#print(local_var)

#we are able to reuse the variable name local_var as the variable is only set in the scope of this
#function
def my_function_2():
    local_var = "I am local to my_function_2"


#if statement variable are global and not locally defined
if True:
    if_var = "I am inside an if statement"

#accessing variable that was created inside an if statement
print(if_var)

#for loop variables are also instantiated as global variables and are able to be accessed outside
#of the for loop
for i in range(3):
    loop_var = "I am inside a loop"

#Below print statement accesses variable that was instantiated inside of the above for loop.
print(loop_var)

#Function Scope & Global Scope

#As functions are the only variables that are local, for/while loops and if statements locally
#deinfed variables are able to be accessed globally. In python the only local variables that are not
#able to be accessed are variables that are defined inside of a function.