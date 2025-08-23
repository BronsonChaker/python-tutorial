#Strings

#print string hello world
print("Hello World")

#single quotes can be used for strings also
print('Hello World')

#strings can contain digits
print("3.141592")

#strings can also contain special character
print("!@$%^&*()-=[];',./")

#set my_string variable to string
my_string = "Hello World!"

#print out string variable
print(my_string) #Output = Hello World!

#print a certain index of my_string,
print(my_string[8]) #Output =  r

#negative value starts from the end of array
print(my_string[-1]) #Output = !

#range index can be print out of a string
print(my_string[3:8]) #Output = lo Wo

#if you leave index number out of start it will begin the start of range -> 8
print(my_string[:8]) #Output = Hello Wo

#if you leave index number out of end it will begin the start of range -> 8
print(my_string[3:]) #Output = lo World!

#will start at index -9 and end at index -4
print(my_string[-9:-4]) #Output = lo Wo

#will start at beginning of string and continue to index -4
print(my_string[:-4]) #Output = Hello Wo

#will start at index -9and finish at the end of string
print(my_string[-9: ])

#will start at index 3 and finish at index -4
print(my_string[3:-4]) #Output = lo Wo

#---------------------------------------------#
#Printing with quotes

# 'Hello World!' instead of Hello World!
my_string_1 = "'Hello World!'"
print( my_string_1 )

# "Hello World!" instead of Hello World!
my_string_2 = '"Hello World!"'
print( my_string_2 )

#Escape sequences can also be used to integrate quotes into output
print( "\'Hello World!\'")

#To print World! onto new line
print( "Hello \nWorld!" )

#To create a tab space between words onto new line
print( "Hello\tWorld!" )

#To implement a backslash you have to utilise a double backslash
print( "\'Hello World!\\'")

#---------------------------------------------#

#Concatenation

#Concatenating two strings together
my_string = "Hello"
my_string += " World!"

print(my_string)

#Concatenating a string and int
my_string = "my Int is:"
my_Int = 5
my_string += str(my_Int)

#---------------------------------------------#

#Methods

my_string = "Hello World"

#Below len method give us the length of the string passed in
print( len(my_string) )

#returns a boolean value depending on if all letters are lowercase or not
#Does not check spaces numbers or punctuation
print(my_string.islower())

#returns a boolean value depending on if all letters are uppercase or not
#Does not check spaces numbers or punctuation
print(my_string.isupper())

#checks if every letter of the string is a letter or not, if there is a space this will be false
print(my_string.isalpha())

#checks if all characters inside the string is a digit
print(my_string.isdigit())

#checks if all characters are alphanumeric, either a letter or number
print(my_string.isalnum())

#checks if all characters of a string is space
print(my_string.isspace())

#checks if my_string variable starts with passed in string value
print(my_string.startswith("Hello"))

#checks if my_string variable end with passed in string value
print(my_string.startswith("World"))

#prints string in lowercases, does not affect the capitalisation of the original string
print(my_string.lower())

#this will change the string variable to all lowercases permanently
my_string = my_string.lower()

#prints string in uppercase, does not affect the capitalisation of the original string
print(my_string.upper())

#this will change the string variable to all uppercase permanently
my_string = my_string.upper()

#prints start of string with a capital letter
print(my_string.capitalize())

#capatalizes the start of the string until changed
my_string = my_string.capitalize()

#First letter of eah words is capitalized
my_string = my_string.title()

#Changes all uppercase to lowercase and all lowercase to uppercase
my_string.swapcase()

#removes all spaces(white space) at the start and end of string
my_string.strip()

#removes all spaces(white space) at the start of the string
my_string.lstrip()

#removes all spaces(white space) adn the end of the string
my_string.rstrip()

#below line of code sets string to lower case and removes white space at start and end of string
print(my_string.lower() .strip())

#this will replace the first passed in word of the string to the second
print(my_string.replace("World", "Python"))

#This will find the first instance of the passed in string in the string variable
#and return an index location of where this starts from
print(my_string.find("World"))

#This will count the amount of times the substring is in the string variable
print(my_string.count("World"))

