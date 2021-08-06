
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())    
    d = dict(input().strip().split() for x in range(n))
    while True:
        try:
            name = input()
            if name in d:
                print('%s=%s' % (name, d[name]))
            else:
                print('Not found')
        except:
            break
