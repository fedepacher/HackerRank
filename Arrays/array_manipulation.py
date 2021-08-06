import time
import math
import os
import random
import re
import sys

def arrayManipulation(n, queries):
    array = [0] * (n + 1)
    for query in queries: 
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k
    max_value = 0
    running_count = 0
    for i in array:
        running_count += i
        if running_count > max_value:
            max_value = running_count
    return max_value
    """ a = [0]*n
    for sub_arr in queries:
        i = sub_arr[0] - 1
        j = sub_arr[1] - 1
        while j - i >= 0:
            a[i] += sub_arr[2]
            i += 1
    return max(a) """

            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout   # stdout is already an open stream
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
