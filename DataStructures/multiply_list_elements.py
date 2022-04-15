#! /usr/bin/env python3

lstIn = [4,3,2,1]

def multy(lstIn):
    prod = lstIn[0]
    for i in range(1,len(lstIn)):
        prod *= lstIn[i]
    return prod

print(str(multy(lstIn)))


#use reduce function
