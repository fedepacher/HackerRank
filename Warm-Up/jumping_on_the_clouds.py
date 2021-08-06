import time
import math
import os
import random
import re
import sys

# 0 0 1 0 1 0 0
def jumpingOnClouds(c):
    cont_saltos = 0
    cont_ceros = 0
    i = 0
    while i < len(c):        
        if c[i] == 0:
            cont_ceros += 1
        if c[i] == 1:
            cont_saltos += 1
            cont_ceros = 0
        if cont_ceros > 1 and cont_ceros <= 2:
            cont_saltos += 1
        else:
            if cont_ceros > 2:
                cont_ceros = 1
        i += 1
    return cont_saltos


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout   # stdout is already an open stream
    
    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()