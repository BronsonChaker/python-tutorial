#Data Structures

#-----------------------------#

#Lists

#Lists can contain Floats, Integers, Strings

#List Example - Integers
my_list = [1, 2, 3, 4, 5]

#List Example - Floats
my_list = [1.0, 2.0, 3.0, 4.0, 5.0]

#List Example - Strings
my_list = ['H', 'e', 'l', 'l', 'o']

#Below example shows how we can convert a string into a list such as ['H', 'e', 'l', 'l', 'o']
                                                            #indexs    0    1    2    3    4
my_list = list("Hello")

#print certain indes of string List
print(my_list[0])

#print range of index for string list
print(my_list[1:3])

#List can have any data type stored inside of them simultaneously, below example has Integer, Float, Boolean and String
#store inside the list
my_list = [1, 2.0, 3.0, True, 'Hello']

#Lists can also be nested
my_list = [[88,99], 3.0, True, 'Hello']

#Below is an example of hwo to select a certain index inside of a nested list inside the nested section
#This will print index 0 of the outer section of the nested list then index 0 of the inner list
print(my_list[0][1])

#-----------------------------------------_#

#List - Modifying Elements

#Below Examples Modifies and element in the List
my_list = list("Hello")
my_list[2] = 'B'
print(my_list)

#-----------------------------------------------------#

#List - Append Method

#Example of Appedning List and adding Integer to the end of list
my_list = [1, 2, 3, 4, 5]
my_list.append(99)
print(my_list)

#-----------------------------------------------------#

#List - Insert Method

#Below example of inserting an element into the list, inside of the insert method parenthesis, the index and the data has 
#to be passed into this
my_list = [1, 2, 3, 4, 5]
my_list.insert(1, 99)
print(my_list)

#-----------------------------------------------------#

#List - Extend Method

#Below extend method is used on a List, this extend method adds the passed in integers to the end of the list
my_list = [1, 2, 3, 4, 5, 88 ,99]
my_list.extend([88, 99])
#Below remove method for list will remove the passed in value from the list, if there is multiple in the list it will remove
#the first found element that is matching
my_list.remove(88)
print(my_list)

#-----------------------------------------------------#

#List - Pop Method

#Below example show the use of the pop methos for lists, the pop method will remove the element at the end of the list
#The pop methos removes it from the list but also returns it, so the popped variable can be assingeed to a variable
my_list = [1, 2, 3, 4, 5, 88 ,99]
my_list.pop()
print(my_list)

#Below example is the utilisation of the pop method, but with an argument this time, this argument refers to the index of the 
#list. This can be a positive or negative index
my_list = [1, 2, 3, 4, 5, 88 ,99]
my_list.pop(2)
print(my_list)

#-----------------------------------------------------#

#List - Delete Method

#Below exmaple uses the del method to delete an element at a certain index, or a certain range, or even full delete a list.
#The elements do not get returned, they are jsut deleted
my_list = [1, 2, 3, 4, 5, 88 ,99]
#deleting a certain index of the list
del(my_list[0])
print(my_list)
#deleting a range of elements from a list.
del(my_list[2:4])
print(my_list)
#deleting a whole list
del(my_list)

#-----------------------------------------------------#

#List - Sort Method

#Below exmaples is Sorting a List
my_list = [1, 3, 5, 2]
my_list.sort()
print(my_list)

#---------------------------------------------------------#
#SETS
#---------------------------------------------------------#

#In sets we can have elements from different datatypes such as Integer, Float, Boolean, and String
#Inside of sets duplicate values are not allowed!
#sets do not have indexes

#Example of Set instantiaion variable_name = {}
my_set = {1, 2.0, 2.0, True, 'Hello'}

#Below example is converting a list containing duplicate elements into a set.
my_list = [1, 1, 1, 1, 1, 1, 1, 1]
#creating an empty set
my_set = set(my_list)
print(my_set) #Output = {1}

my_set = {1, 2, 3, 4, 5}


#Set - Add method
#add() is used to add an element into the specified set
my_set.add(5)
print("Add Method", my_set)

#Set- Update method
#update() is used to add arguments into the specificied set
my_set.update({4,5,6,7})
print("Update Method", my_set)

#Set - Remove Method
#remove() used to remove the argument value specified from the set, if the lsit does not contain the argument, this will
#throw an error. Because of this it is bettter to use discard() instead
my_set.remove(1)
print("Remove Method", my_set)

#Set - Discard Methond
#discard() is used to discard and element in a list, if the element is not inside the list it will now throw an error, this
#is preferred over the remove method for this reason
my_set.discard(2)
print("Discard Method", my_set)

#Set - Clear Method
#clear() is used to clear all elements from a set
my_set.clear()
print("Clear Method", my_set)

#Set - Union Set
#Below exmaples is creating a union set, combining two sets
my_set_1 = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}

#Example 1 of creating a union set with two sets using the or operator
union_set = my_set_1 | my_set_2
#Example 2 of creating a union set with two sets using the union method and an argument
union_set = my_set_1.union(my_set_2)
print(union_set)

#Set - Inter Set (Intersection)
my_set_1 = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}

#Example 1 of creating an inter set with two sets using the and operator
inter_set = my_set_1 & my_set_2
#Example 2 of creating an inter set with two sets using the intersection method and an argument
inter_set = my_set_1.intersection(my_set_2)
print(inter_set)










