N, M = tuple(map(int, input().split()))

lst = list(map(int, input().split()))
set_lst = set(lst)

A = set(map(int, input().split()))
B = set(map(int, input().split()))

X = A.intersection(set_lst)
Y = B.intersection(set_lst)

Z = X.difference(Y)

lst_dict = {}

happy = 0
for i in list(Z):
    happy += lst.count(i)
        
print(happy)