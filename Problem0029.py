'''
-> Task 0029:

You are given a 2-D array with dimensions N X M.
Your task is to perform the min function over axis 1 and then find the max of that.

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n, m = tuple(map(int, input().split()))
lst = [] 
for i in range(n):
    row = list(map(int, input().split()))
    lst.append(row)
arr = np.array(lst)

mins = np.min(arr ,axis = 1)
mx = np.max(mins)
print(mx)
