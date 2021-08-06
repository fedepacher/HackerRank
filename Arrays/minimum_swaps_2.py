import time
import math
import os
import random
import re
import sys


def minimumSwaps(arr):
    arr = [p - 1 for p in arr]
    moves = 0
    i = 0
    while i < len(arr):
        if abs(arr[i] - i) > 0:
            moves += 1
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        else:
            i +=1
    return moves
            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout   # stdout is already an open stream
    
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

