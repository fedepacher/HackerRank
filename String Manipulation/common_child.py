import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def commonChild(s1, s2):
    obj1 = Counter(s1)
    obj2 = Counter(s2)
    obj3 = obj2 - obj1
    obj4 = obj2 & obj1
    obj5 = obj2 | obj1
   
if __name__ == '__main__':
    fptr = sys.stdout

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

