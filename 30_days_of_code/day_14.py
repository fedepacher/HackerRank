import time
import math
import os
import random
import re
import sys

class Difference:
    def __init__(self, a):
        self.__elements = a
        

    def computeDifference(self):
        self.__elements.sort()
        self.maximumDifference = abs(self.__elements[0] - self.__elements[len(self.__elements) - 1])
            


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)