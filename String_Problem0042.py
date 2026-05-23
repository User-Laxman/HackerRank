#!/bin/python3

import math
import os
import random
import re
import sys

'''
->TASK0042:
"alison heck" should be capitalised correctly as "Alison Heck".

Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
'''
# Complete the solve function below.
def solve(s):
    s = s.title()
    lst = s.split(' ')
    st_lst = []
    for word in lst:
        st_lst.append(word.capitalize())
    return ' '.join(st_lst)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
