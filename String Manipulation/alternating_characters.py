import math
import os
import random
import re
import sys
#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def alternatingCharacters(s):
    first_c = s[0]
    i = 1
    count = 0
    while i < len(s):
        if first_c == s[i]:
            count += 1
        else:
            first_c = s[i]
        i += 1
    return count


if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

