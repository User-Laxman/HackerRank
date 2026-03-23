'''
->Task0027:
You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A.

Note: use numpy.set_printoptions(legacy = '1.13')
'''

import numpy as np
lst = list(map(float, input().split()))
arr = np.array(lst)
np.set_printoptions(legacy = '1.13')
print(np.floor(arr))
print(np.ceil   (arr))
print(np.rint(arr))
