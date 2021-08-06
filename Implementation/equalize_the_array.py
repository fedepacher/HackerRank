import time
import math
import os
import random
import re
import sys


def equalizeArray(arr):
    my_dic = {i:arr.count(i) for i in arr}    
    m = max(my_dic, key=my_dic.get)
    del my_dic[m]
    cont = 0
    for k, v in my_dic.items():
        cont += v
    return cont


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout   # stdout is already an open stream
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()