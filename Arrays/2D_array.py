import time
import math
import os
import random
import re
import sys


def hourglassSum(arr):
    max = float('-inf')
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            a = arr[i+0][j+0]
            b = arr[i+0][j+1]
            c = arr[i+0][j+2]
            d = arr[i+1][j+1]
            e = arr[i+2][j+0]
            f = arr[i+2][j+1]
            g = arr[i+2][j+2] 
            sum = a + b + c + d + e + f + g
            if sum > max:
                max = sum
    return max


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout   # stdout is already an open stream
    
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
