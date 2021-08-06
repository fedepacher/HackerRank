import time
import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def countingValleys(steps, path):
    cont = 0
    cont_v = 0
    flag_v = False
    for i in range(steps):
        if path[i] == 'D':
            cont -= 1
            flag_v = True
        else:
            cont += 1
            flag_v = False
        if cont == 0 and not flag_v:
            cont_v += 1
    return cont_v 


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout   # stdout is already an open stream
    
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()