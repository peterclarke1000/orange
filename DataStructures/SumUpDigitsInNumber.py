#! /usr/bin/env python3

# add all digits in a number

def add_digits_1(num):
    '''
    using modulus to pick off last digit and using divide by 10 to index left
    '''
    sum = 0
    while num > 0:
        digit = num%10
        sum = sum + digit
        num = int(num/10)
        print()
    return sum

def add_digits_2(num):
    '''
    Converting the number to a string, picking off digits 1 by 1
    casting back to integers and adding them
    '''
    strNum = str(num)
    for i in range(len(strNum)):
        if i == 0:
            sum = int(strNum[0])
        else:
            sum = sum + int(strNum[i])
    return sum

def add_digits_3(num):
    '''
    Converting the number to a string, so I can iterate over the string 
    picking off digits 1 by 1 and type casting back to integers and 
    adding them together to calculate the sum
    '''
    strNum = str(num)
    sum = 0
    for i in range(len(strNum)):
            sum = sum + int(strNum[i])
    return sum


def add_digits_4(num):
    '''
    convert the elements to a string and iterate over the. 
    Convert back to integer to add
    '''
    sum = 0
    lstNum = list(str(num))
    for i in lstNum:
        sum = sum + int(i)
    return sum    

def add_digits_5(num):
    '''
    using reduce function. Explicitly importing reduce 
    from func tools here to hammer home the point that it's been moved in python 3.x
    '''
    from functools import reduce
    lst_nums = map(lambda x : int(x),list(str(num)))
    sum = reduce(lambda x,y: x+y,lst_nums)
    return sum
def add_digits_6(num):
    '''
    This time I want to transform the number into a list of integers 
    in a single statement
    '''

    sum = 0
    lst_ints = map(lambda x: int(x),list(str(num)))
    for i in lst_ints:
        sum = sum + i
    return sum
    



# print(add_digits_1(341))
# print(add_digits_2(341))
# print(add_digits_3(341))
# print(add_digits_4(341))
# print(add_digits_5(341))
print(add_digits_6(341))

