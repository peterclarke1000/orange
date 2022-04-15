#! /usr/bin/env python3


class myrange:
    def __init__(self,start,end):
        self.value = start
        self.end = end

    # for something to be iterable it needs to have a __iter__ method
    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value +=1
        return current
    


nums = myrange(1,10)
print(dir(nums))
for num in nums:
    print(num)
