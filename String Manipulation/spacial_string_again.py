import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def substrCount(n, s):
    count = n
    for x in range(n): 
        y = x
        while y < n - 1:
            y += 1
            if s[x] == s[y]:
                count += 1
            else:
                if s[x:y] == s[y+1:2*y-x+1]:
                    count += 1
                break

    return count



    # l = list(s)    
    # c = Counter(l)
    # if len(c) == 1:
    #     count = 0
    #     for i in range(n + 1):
    #         count += i
    #     return count
    # count = n
    # for elem in c.items():
    #     if elem[1] > 1:
    #         a = [i for i, x in enumerate(l) if x == elem[0]]
    #         for i in range(len(a) - 1):
    #             if abs(a[i] - a[i+1]) <= 2:
    #                 count += 1 
    # return count



if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

