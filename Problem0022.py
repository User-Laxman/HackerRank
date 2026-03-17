'''
->Task0022:
You are given a N X M integer array matrix with space separated elements
(N = rows and M = columns).
Your task is to print the transpose and flatten results.
'''
import numpy as np 
lst = list(map(int, input().strip().split()))
arr = np.array(lst)
arr.shape = (3,3)
print(arr)

