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

def maximumToys(prices, k):
    prices.sort(reverse=False)
    accum=0
    count = 0
    for el in prices:
        if accum + el < k:
            accum += el
            count += 1
    return count


if __name__ == '__main__':
    fptr = sys.stdout   # stdout is already an open stream
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
