import math
import os
import random
import re
import sys

class Calculator():
    def __init__(self) -> None:
        pass

    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception ('n and p should be non-negative')
        return pow(n, p)


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   