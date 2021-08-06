import time
import math
import os
import random
import re
import sys
from collections import Counter

def checkMagazine(magazine, note):
    obj1 = Counter(magazine)
    obj2 = Counter(note)
    obj3 = obj2 - obj1
    if obj3 == {}:
        print("Yes")
        return
    print("No")
    return

    """ magazine_n = set(magazine)
    note_n = set(note)
    my_dic_note = {i:note.count(i) for i in note}
    my_dic_mag = {i:magazine.count(i) for i in magazine}
    note_rep_word = set([x for x in note if note.count(x) > 1])
    new = magazine_n & note_n
    if new == note_n:
        if len(note) == len(note_n):
            print("Yes")
            return
        else:
            for k in note_rep_word:
                if my_dic_mag[k] < my_dic_note[k]:
                    print("No")
                    return
    else:
        print("No")
        return
    print("Yes")
    return """
    
    """ magazine_n = set(magazine)
    note_n = set(note)
    my_dic = {i:note.count(i) for i in note}
    new = magazine_n & note_n
    if new == note_n:
        for k,v in my_dic.items():
            if v > magazine.count(k):
                print("No")
                return
    else:
        print("No")
        return
    print("Yes")
    return """

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout   # stdout is already an open stream
    
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)