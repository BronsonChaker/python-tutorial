#----------------------------------#
    #Coding Exercise #38
#----------------------------------#
def is_vowel(letter):
    vowels = "aeiou"
    if letter in vowels:
        return True
    else:
        return False
    
#----------------------------------#
    #Coding Exercise #39
#----------------------------------#
def reverse_string(text):
    return text[::-1]

#----------------------------------#
    #Coding Exercise #40
#----------------------------------#
def remove_vowels(text):
    result = ""
    
    vowels = "aeiou"
    
    for char in text:
        if char not in vowels:
            result += char
    
    return result

#----------------------------------#
    #Coding Exercise #41
#----------------------------------#
def replace_spaces(text):
    result = ""
    for char in text:
        if char == " ":
            result += "-"
        else:
            result += char
    return result

#----------------------------------#
    #Coding Exercise #42
#----------------------------------#
def convert_temperature(temp, unit):
    
    if unit == "F":
        return (temp - 32) * 5/9
    elif unit == "C":
        return (temp * 9/5) + 32
    else:
        return None
#----------------------------------#
    #Coding Exercise #43
#----------------------------------#
def second_largest(numbers):
    
    first = float('-inf')
    second = float('-inf')
    
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second
#----------------------------------#
    #Coding Exercise #44
#----------------------------------#
def is_ascending(numbers):
    
    for i in range(len(numbers) - 1):
        
        if numbers[i] >= numbers[i + 1]:
            return False
            
    return True
#----------------------------------#
    #Coding Exercise #45
#----------------------------------#
def first_repeating_number(nums):
    
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]

    return None
#----------------------------------#
    #Coding Exercise #46
#----------------------------------#
def first_repeating_number(nums):
    seen = set()
        
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
            
    return None
#----------------------------------#
    #Coding Exercise #47
#----------------------------------#
def find_duplicates(numbers):
    
    seen = set()
    duplicates = set()
    
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)
#----------------------------------#
    #Coding Exercise #48
#----------------------------------#