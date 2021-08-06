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


def get_limit(f,d):
    count = 0 
    m1,m2 = (d//2,d//2+1)
    m = []
    for i,j in enumerate(f):
        count+=j
        if not m and m1<=count:
            m.append(i)
        if m2<=count:
            m.append(i)
            break
    return m[-1]*2 if d%2 else sum(m)
    
def activityNotifications(expenditure, d):
    f = [0]*201
    count = 0
    for i in expenditure[:d]:
        f[i]+=1
    for i,v in enumerate(expenditure[d:]):
        limit = get_limit(f,d)
        if v>=limit:
            count+=1
        f[v]+=1
        f[expenditure[i]]-=1
    return count




# def activityNotifications(expenditure, d):
#     flag_par = False
#     if d % 2 == 0:
#         flag_par = True
#     count = 0
#     index = d//2
#     for i in range(len(expenditure) - d):
#         a = expenditure[i:d + i]
#         a.sort(reverse=False)
#         media = a[index]
#         if flag_par:
#             media += a[index + 1]
#             media = media / 2
#         if media * 2 <= expenditure[d + i]:
#             count += 1
#     return count


if __name__ == '__main__':
    fptr = sys.stdout   # stdout is already an open stream

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
