'''
->Task0031:
You are given two arrays A and B. Both have dimensions of N X M.
Your task is to compute their matrix product.
'''


import numpy as np
N = int(input())
A = []
B = []
flag = False
for i in range(1, N*2+1):
    if i%(N+1)==0:
        flag = True
    if not flag:
        A.append(list(map(int, input().split())))
        continue
    B.append(list(map(int, input().split())))

a_arr = np.array(A)
b_arr = np.array(B)

print(np.dot(A, B))