import time
import math
import os
import random
import re
import sys


def rotLeft(a, d):
    a[:]=a[d:len(a)]+a[0:d]
    """ for i in range(d):
        aux = a[0]
        for i in range(len(a)-1):            
            a[i] = a[i+1]
        a[len(a)-1]=aux """
    return a
            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout   # stdout is already an open stream
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

