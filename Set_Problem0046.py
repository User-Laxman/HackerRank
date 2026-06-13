'''
->TASK0046:
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in ser B. Your initial happiness is 0. For each i integer in the array, if i in A. you add 1 to your happiness. if i in B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happinesss at the end

SOLUTION:
lst = [...N]
A = [...M]
B = [...M]

set_list = set(list)

X = A intersection set_list
Y = B intersection set_list

Z = X intersection Y

X-NEW = X - Z, Y-NEW = Y - Z

from X-NEW count repeat of each number in 'list' and add to happiness
from Y-NEW count repeat of each number in 'list' and substract to happiness
'''

N, M = tuple(map(int, input().split()))

lst = list(map(int, input().split()))
set_lst = set(lst)

A = set(map(int, input().split()))
B = set(map(int, input().split()))

X = A.intersection(set_lst)
Y = B.intersection(set_lst)

Z = X.intersection(Y)

X_new = X.difference(Z)
Y_new = Y.difference(Z)

happy = 0
for i in list(X_new):
    happy += lst.count(i)
for i in list(Y_new):
    happy-=lst.count(i)
print(happy)
