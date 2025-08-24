#Loops

#Simple while loop which continues until num is less than 3(2). Inside the body of the loop it iterates
#num += 1 every loop
num = 0
while num < 3:
    num += 1
    print( num )

#Loop is also used below, instead of utilising a conditional to break out the while loop, we break out the while loop
#inside the if statement
num = 0
while True:
    if num >= 3:
        break
    num += 1
    print( num )


#Below loop skips even numbers when printing using the continue keyword
num = 0
while True:
    if num >= 3:
        break
    num += 1
    if num % 2 == 0:
        continue
    print(num)

#-------------------------------------------------------------------------------#

#Coding Exercise 21 - While Loops Intro
num = 5

while not num < 1 :
    print( num )
    num-= 1

# -------------------------------------------------------------------------------#

#For Loops

#for the for loop parameters range(stop)
#for the for loop parameters range(start, stop)
#for the for loop parameters range(start, stop, step)

#start - the point we are starting the iteration from
#stop - the point we are stopping the iteration for 1 this would be 0 as it goes to but is not inclusive of this number
#step - the iteration that is being performed e.g 1 or -1

#Below for loop will run 3 times and print out num everytime, if not using the variable inside the body of the for loop
#set for _ in range(3)

num = 0
print(f"{"For Loop":^18}")
for num in range(num, 3, 1):
    print(num)

#---------------------------------------------------------------------------------#

#Coding Exercise 22 - For Loops - Range Based

for num in range(5, 0, -1):
    print(num)

#---------------------------------------------------------------------------------#

#Nested For Loop

#outer loop runs first then the inner loop runs until the condition is met then this repeats until the condition of the
#outler loop has been met
for num_1 in range(2):
    for num_2 in range(2):
        print(num_1, num_2)

# ---------------------------------------------------------------------------------#

#Coding Exercise 24 - Nested Loops
for num_1 in range(10):
    for num_2 in range(10):
        print(num_1, num_2)

#---------------------------------------------------------------------------------#

#Iterating Over Collections

#iterating over a string
for char in "Hello":
    print(char)

#Iteration over a List
fruits = ["apple", "banana", "cheery"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry

#---------------------------------------------------------------------------------#

#While Loop vs For Loop

#While Loop in Linked List
#If you do not know the amount of elements inside of the linked list, it is better to use a while loop 
#as it will continue until a condiition has been met, in a Linked List this would be for example until node.next is null
#if you are traversing a list.

#For Loop in Linked List
#If you knwo the amount of elemnts or length of a Linked List you can give the for loop a range in which
#it can traverse the Linked List from start to finsih

#---------------------------------------------------------------------------------#



