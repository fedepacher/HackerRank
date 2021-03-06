import collections
import time
import math
import os
import random
import re
import sys
from collections import Counter

def sherlockAndAnagrams(s):
    buckets = {}
    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            key = frozenset(Counter(s[i:i+j]).items()) # O(N) time key extract
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    for key in buckets:
        count += buckets[key] * (buckets[key]-1) // 2
    return count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout   # stdout is already an open stream
    
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()