#----------------------------------#
    #Coding Exercise #31
#----------------------------------#
def even_or_odd(number):
    if (number % 2 == 0):
        return "even"
    else:
        return "odd"
 
#----------------------------------#
    #Coding Exercise #32
#----------------------------------#
def maximum(a, b):
    if(a > b):
        return a
    else:
        return b
#----------------------------------#
    #Coding Exercise #33
#----------------------------------#
def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum+=num
    return sum
#----------------------------------#
    #Coding Exercise #34
#----------------------------------#
def repeat_word(word, count):
    if count == 0:
        return ""
    else:
        return word*count
    
#----------------------------------#
    #Coding Exercise #35
#----------------------------------#
def count_a(text):
    count = 0

    for letter in text:
        if letter == 'a':
            count += 1
            
    return count

#----------------------------------#
    #Coding Exercise #36
#----------------------------------#
def sum_digits(text):
    sum = 0
    
    for char in text:
        digit = int(char)
        sum += digit
    
    return sum

#----------------------------------#
    #Coding Exercise #37
#----------------------------------#
def count_evens(numbers):
    count = 0
    
    for num in numbers:
        if num % 2 == 0:
            count += 1
    
    return count
