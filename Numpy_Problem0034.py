'''
-> TASK0034:
You are given a square matrix A with dimensions N X N. 
Your task is to find the determinant. 
Note: Round the answer to 2 places after the decimal.
'''

import numpy as np

#linalg.det computes and returns determinant of an array
#linalg.eig computes and returns eigen values and eigen vectors of an array
#linalg.inv computes and returns inverse of an array

N = int(input().strip())

lst = []
for i in range(N):
    row = list(map(float, input().strip().split()))
    lst.append(row)

arr = np.array(lst)
det = round(np.linalg.det(arr), 2) #Using linear algebra

print(f"{det}")