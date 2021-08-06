import time
import math
import os
import random
import re
import sys


def repeatedString(s, n): 
    long_s = len(s)
    char_rep = s.count('a')
    div = n / long_s    
    div_ent = int(div)
    div_frac = div - div_ent # porcentaje de lo que falta 
    peso_char = 100 / long_s
    count = char_rep * div_ent
    if div_ent > 0:
        if div_frac > 0:
            k = 0
            f = div_frac * 100
            f1 = int(div_frac * 100)   
            f2 = f - f1  
            if f2 > 0.5:
                f1 += 1 
            i = 100 - f1
            while( i < 100):
                if s[k] == 'a':
                    count += 1
                k += 1
                i += peso_char 
                if k > long_s:
                    break
    else:
        k = 0
        for i in range(n):
            if s[k] == 'a':
                count += 1
            k += 1
            if k >= len(s):
                k = 0
    return count
         

    """ k = 0
    cont_a = 0
    for i in range(n):
        if s[k] == 'a':
            cont_a += 1
        k += 1
        if k >= len(s):
            k = 0
    return cont_a """


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout   # stdout is already an open stream
    
    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()