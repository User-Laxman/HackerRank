'''
->Task0023:
You are given two integer arrays of size n X p and m X p (n & m are rows, and p is the column).
Your task is to concatenate the arrays along axis 0.
'''

import numpy as np

N, M, P = tuple(map(int, input().split()))

lst1 = [list(map(int, input().split())) for _ in range(N)]
lst2 = [list(map(int, input().split())) for _ in range(M)]
lst1.extend(lst2)

arr = np.array(lst1)

print(arr)
