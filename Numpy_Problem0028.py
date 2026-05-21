'''
->Task0028:
You are given a 2-D array with dimensions N X M.
Your task is to perform the 'sum' tool over axis 'product' and then find the  of that result.
'''

import numpy as np
N, M = tuple(map(int, input().split()))
lst = [list(map(int, input().split())) for _ in range(N)]
arr = np.array(lst)
arr = np.sum(arr, axis = 0)
print(np.prod(arr, axis = None))
