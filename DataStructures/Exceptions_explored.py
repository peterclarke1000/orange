#! /usr/bin/env python3

# builds a nums list object
nums = [i for i in range(5)]

#Obiviously we can use this nums lst as an iterable object in a for loop

for i in nums:
    print(i)

print('\n\n' + '*'*30 + '\n\n')

# To explore iterators and exceptions
# First we'll need to create an iterator out of our nums list
# i_nums = iter(nums)
i_nums = nums.__iter__()
# Now we need to use this iterator and it's next attribute in a while
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break


