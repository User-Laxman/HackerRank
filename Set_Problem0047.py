'''
->TASK0047:
input two sets of different sizes,
output there symmetric difference: union of two sets except common elements 
in sorted order

'''

N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = set(map(int,input().split()))

result = sorted(list(A.difference(B).union(B.difference(A))))
for i in result:
    print(i)