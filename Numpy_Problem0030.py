'''
Task0030: 
You are given a 2-D array of size N X M.
Your task is to find:

The mean along axis 1
The var along axis 0
The std along axis None

'''
import numpy as np
N,M = tuple(map(int, input().split()))
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
arr = np.array(lst)
print(arr.mean(axis = 1))
print(arr.var(axis = 0))
print(arr.std(axis = None).round(11))