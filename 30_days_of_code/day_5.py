
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    num = 10
    for i in range(max(num, 0)):
        print(f"{n} x {i + 1} = {n * (i + 1)}")