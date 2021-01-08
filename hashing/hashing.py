#!/usr/bin/python3
##########################################
# Date: January  8, 2020
# Purpose:  Trying out the builtin hash() function. I learned that you cannot hash mutable data types like lists, sets or dictionaries. Object must be mutable like a Tuple
##########################################
count = int(input())
x = str(input())
y = tuple(map(int, x.split(' ')))
z = hash(y)
print (z)


