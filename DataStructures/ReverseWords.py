#! /usr/bin/env python3
from ctypes.wintypes import WORD
from itertools import islice as slice

'''
Reversing words in a string
'''
# Approach 1 (using slice)
def reverseWords1(strIn):
    # createa list from string with split and then use slice to reverse it.
    # lastly joing the list elements to for the reversed string
    words = strIn.split(' ')[::-1]
    strOut = " ".join(words)
    return strOut

# Approach 2 (using split and a for loop)
# create a list from string with split and 
# use a for look to reverse the list
# using join to rebuild the reversed string
def reverseWords2(strIn):
    words = strIn.split(' ')
    lstOut = []
    for word in words:
        lstOut.insert(0,word)
    strOut = " ".join(lstOut)
    return strOut

# Approach 3  (using a word swapping approach)
def reverseWords3(strIn):
    '''
    This approach is convert the string to a list and start swapping list elements from the middle
    '''
    
    # check to see if there is an even or odd number of words in string
    lstIn = strIn.split(' ')
    l = int(len(lstIn))
    evenNum = True if l%2 ==0 else False

    if evenNum: # if even
        # Find the middle word
        m = int(l/2)
    else:   # if odd
        # Find middle word
        m = int(l/2 + 1)

    # use a while loop to swap the words
    # starting from the middle start swapping words at the jth position and the num
    while (m <= l-1):
        lstIn[m], lstIn[l - m - 1] = lstIn[l - m - 1], lstIn[m]
        m +=1
    strOut = ' '.join(lstIn)    
    return strOut    

# Approach 4  (using split and while loop)
def reverseWords4(strIn):
    '''
    This approach is convert the string to a list and then use while loop to rebuild
    the list in reverse
    '''

    lstIn = strIn.split(' ')
    lstOut = []
    l = len(lstIn)
    x = 0
    while x <= l-1:
        # lstOut.insert(0,word)
        lstOut.insert(0,lstIn[x])
        x +=1
    strOut = ' '.join(lstOut)
    return strOut    


        


strIn = "Peter Clarke Woz Here so!"

print(reverseWords1(strIn))
print("***************"*2)
print(reverseWords2(strIn))
print("***************"*2)
print(reverseWords3(strIn))
print("***************"*2)
print(reverseWords4(strIn))
