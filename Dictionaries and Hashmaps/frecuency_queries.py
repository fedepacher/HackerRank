import collections
import time
import math
import os
import random
import re
import sys
from collections import Counter
from collections import defaultdict
import time

def freqQuery_el(queries):    
    results = []
    arr = dict()
    freq = defaultdict(int)
    for x in queries:
        ops, value  = x    
        initial = arr.get(value, 0)
        if ops == 3:            
                results.append(1 if freq.get(value) else 0)                    
        else:            
                freq[initial] -= 1            
                if ops == 1:
                        arr[value] = initial + 1
                elif ops == 2 and initial:
                        arr[value] -= 1
                freq[arr.get(value,0)] += 1           
    return results



def freqQuery_mio(queries):
    ret_val = []
    d = defaultdict(int)
    for elem in queries:
        k, v = elem
        if k == 1:
            d[v] += 1
        elif k == 2:
            if d[v] > 0:
                d[v] -= 1
        else:
            ret_val.append(1 if v in d.values() else 0)            
    return ret_val



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout   # stdout is already an open stream
    
    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    start_time = time.time()
    ans = freqQuery_mio(queries)
    total_time = str((time.time() - start_time))
    print(f"Tiempo de proceso mio: {total_time} s")

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.write('#########################################################')
    fptr.write('\n')

    start_time = time.time()
    ans = freqQuery_el(queries)
    total_time = str((time.time() - start_time))
    print(f"Tiempo de proceso el: {total_time} s")

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()