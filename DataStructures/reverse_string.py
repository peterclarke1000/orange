#!/usr/bin/env python3
"""
This module has various ways to implement reversing a string. 
when run you will need to pass the string that you want to reverse 
"""

import pdb
import sys
from turtle import pd

class reversestring:
    def __init__(self, reverseMethod, strIn):
        self.reverseMethod = reverseMethod
        self.strIn = strIn

    def reversenow(self):
        '''
        :param strIn is the string to reverse
        :param reverseMethod is the method type to use to reverse the sting
        :return The reversed string.
        '''
        match self.reverseMethod:
            case 'x':
                print(" Exiting")
            case '1':
                print("The reverse of your string is:")
                print(self.reverseWithForLoop(self.strIn))
            case '2':
                print("The reverse of your string is:")
                print(self.reverseWithBltIn(self.strIn))
            case '3':
                print("The reverse of your string is:")
                print(self.reverseWithSlice(self.strIn))
            case '4':
                print("The reverse of your string is:")
                print(self.reverseSomeNewWay(self.strIn))
            case None:
                print("no options presented")

    def reverseWithForLoop(self, strIn):
        ''' 
        reverse the input string by interating over a string with
        a for-loop
        :param strIn  the input string you want to reverse
        :return: strOut is the reversed string.
        '''
        strOut = ""
        for i in (strIn):
            strOut = i + strOut

        return strOut

    def reverseWithBltIn(self, strIn):
        '''
        reverse a string using built in reverse funtion
        param: strIn the input string you want to reverse
        result: strOut is the reversed string
        '''  

        strOut = ''.join(reversed(strIn))
        return strOut

    def reverseWithSlice(self, strIn):
        '''
        reverse a string using built in slice funtion
        param: strIn the input string you want to reverse
        result: strOut is the reversed string
        '''  
        strOut = strIn[::-1]
        return strOut    



        
def menu():
    '''
    '''
    strIn, option = '', ''
    print("Select a way to reverse a string")
    print("\t 1: Enter 1 to use for-loop method")
    print("\t 2: Enter 2 to use builtin_reversed method")
    print("\t 3: Enter 3 to use slice")
    print("\t x: enter x to exit the program")
    print(">>  ",end="")
    option = str(input())
    print("")
    if option != 'x':
        print("Enter the string you want to reverse")
        print(">>  ",end="")
        strIn = str(input())
 
    return option, strIn



def main(option, strIn):
    ''' 
    Do this
    Returns the other.

    :param option is the type of reverse method you want to use
    :param strIn is the string you want to operate on
    :return the reversed string will be returned.
    '''
   
    run = reversestring(option, strIn)
    run.reversenow()
  
    return 0



if __name__ == '__main__':
    option = 'y'
    while option not in 'xn':
        option, strIn = menu()
        main(option,strIn)
        if option != 'x':
            print("keep going y/n")
            print(">>  ",end="")
            option = str(input())
    print("\n Bye.... \n")    
