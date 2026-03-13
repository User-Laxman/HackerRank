'''
->Task15:
The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t
Print the result of hash(t).
'''
n = int(input().strip())
a = map(int, input().strip().split()[:n])
t = tuple(a)
print(hash(t))
