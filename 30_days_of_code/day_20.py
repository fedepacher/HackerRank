#!/bin/python3

import math
import os
import random
import re
import sys

def countSwaps(a):
    firstElement = 0
    lastElement = 0
    numSwaps = 0
    flag = True
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                numSwaps += 1
                lastElement = a[j]
                a[j] =a[j+1]
                a[j+1] = lastElement
    firstElement = a[0] 
    lastElement = a[len(a)-1]
    print(f'Array is sorted in {numSwaps} swaps.')
    print(f'First Element: {firstElement}')
    print(f'Last Element: {lastElement}')
    return

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)