
import math
import os
import random
import re
import sys

def sep(s):    
    s_par = ''
    s_impar = ''
    for i in range(len(s)):
        if i % 2 == 0:
            s_par += s[i]
        else:
            s_impar += s[i]
    return s_par + ' ' + s_impar

if __name__ == '__main__':
    n = int(input().strip())
    data = []
    for i in range(n):
        data.append(input())
    for i in data:
        print(sep(i))
    