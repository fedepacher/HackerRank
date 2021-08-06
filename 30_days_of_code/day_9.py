
import math
import os
import random
import re
import sys

def factorial(n):
    # Write your code here
    if n <= 1:
        return 1
    result = n * factorial(n-1)
    return result

if __name__ == '__main__':
    fptr = sys.stdout 

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
