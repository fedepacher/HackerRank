
import math
import os
import random
import re
import sys

def DecimalToBinary(num):
    cont = 0
    cont_max = 0
    while num > 0:        
        result_aux = num % 2
        if result_aux == 1:
            cont += 1
        else:
            if cont_max < cont:
                cont_max = cont
            cont =0
        num = num // 2
    if cont_max < cont:
        cont_max = cont
    return cont_max
        

if __name__ == '__main__':
    n = int(input().strip())
    print(DecimalToBinary(n))
