import math
import os
import random
import re
import sys
#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def makeAnagram(a, b):
    obj1 = list(a)
    obj2 = list(b)
    result = 0
    if len(obj1) < len(obj2):
        result = fun(obj1, obj2)
    else:
        result = fun(obj2, obj1)
    return result

def fun(obj1, obj2):
    i = 0
    while i < len(obj1):
            elem = obj1[i]
            if elem in obj2:
                obj1.remove(elem)
                obj2.remove(elem)
            else:
                i += 1
        
    return len(obj1) + len(obj2)

if __name__ == '__main__':
    fptr = sys.stdout

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
