import time
import math
import os
import random
import re
import sys
from collections import Counter

def twoStrings(s1, s2):
    obj1 = set(s1)
    obj2 = set(s2)
    obj3 = obj2 & obj1
    if len(obj3) > 0:
        return "YES"
    return "NO"
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout   # stdout is already an open stream
    
    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()