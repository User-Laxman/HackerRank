'''
-->TASK0052:
INPUT:
n1 integers space separated
n2 integers space separated

find the length n1 integers difference n2 integers
'''


n1 = int(input())
english = set(map(int, input().split()))

n2 = int(input())
french = set(map(int, input().split()))

english.difference_update(french)

print(len(english))