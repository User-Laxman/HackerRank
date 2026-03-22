# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np 

N, M = tuple(map(int, input().split()))
lst = [[list(map(int, input().split()[:M])) for __ in range(N)]for _ in range(2) ]

a = np.array(lst[0], dtype = np.int64)
b = np.array(lst[1], dtype = np.int64)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
