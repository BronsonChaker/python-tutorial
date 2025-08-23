#Below will return an int data type
print(5 * 5)

#Below will return a float data type
print(5 * 5.0)

#--------------------------------------#

#Below division operator will return a float type as it is very uncommon that
#dividing will end up as an int
print(5 / 5)

#Below division has a double  forward slash which will ensure an int is the output
print(5 // 5)

print (5 / 3) #returns 1.667

print (5 // 3) #returns 1 as remove all decimal points to the right and keeps the int

#--------------------------------------#

# Modulo
# % = Modulo, give the remainder from the divison

#Below code example shows how we can find if a number is odd or even
print( 7 % 2 ) # Output = 1 // Odd
print( 7 % 2 ) # Output = 0 // Even


#--------------------------------------#

#Exponent

#Below is an example of exponent, Below example is 2 power 3
print( 2 ** 3 ) # Output = 8


#--------------------------------------#

#Assignment Operator
# = <- is an Assignment Operator

#Below example of assigment operator where we are assigning 8 to my_int
my_int = 8

#Assigning new value to my_int =, Adding 1 to my_int
my_int += 1

#Assigning new value to my_int=, Minuting 1 from my_int
my_int -= 1

#Assigning new value to my int, Multiplying my_int by 2
my_int *= 2

#Assigning new value to my int, Dividing my_int by 2
my_int *= 2

#Assigning new value to my int, Modulo my_int by 2
my_int %= 2

#Assigning new value to my int, Exponent my_int by 3
my_int **= 3

#--------------------------------------#

#Comparison Operators

#Can either be True or False

#Basic examples below of comparison operators
print( 5 == 5 ) # Output = True

print( 5 == 4 ) # Output = False

print( 5 == 5.0) # Output = True

print( 5 == "5") # Output = False

print( "5" == "5" ) #Output = True

print( "5" == '5' ) #Output = True

print( 5 != 4 ) #Output = True

print( 5 != 5 ) #Output = False

print( 5 != 5.0 ) #Output = False

print( 5 != "5" ) #Output = True

#Below sample when type checking with assignment operator
print( type(5 == 5) ) # Output = <clas 'bool'>

print(5 > 4) #Output = True

print(5 < 4) #Output = False

print(5 > 5) #Output = False

# print( 5 > "5") #CANNOT DO THIS TYPE ERROR, cannot compare int and string

print( 5>= 5) #Output = True

print(4 <= 4) #Output = True

print(5 >= 5.0) #Output = True

print(4 <= 4.0) #Output = True

#Alphabetical Comparison
print('cats' > 'dogs') #Output = False

print('bbb' > 'aaa') #Output = True

print('BBB' > 'aaa') #Output = False #Based off unicode value

print('cat2' > 'cat1') #Output = True , this traverses cat word until it gets to numbers and comapres unicode

#--------------------------------------#

#Logical Operators

#order of operations
#not -> and -> or

#and examples
print(5==5 and 4==4) #Output = True

print(5==5 and 4>5) #Output = False

print(5==4 and 4==4) #Output = False

print(5<4 or 4>5) #Output = False

#or examples
print(5==5 and 4==4) #Output = True

print(5==5 and 4>5) #Output = True

print(5==4 and 4==4) #Output = True

print(5<4 or 4>5) #Output = False

#not examples
print(not 5==5) #Output = False