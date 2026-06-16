'''
-->TASK0051:
INPUT:
n1 integers space separated
n2 integers space separated

find the length n1 integers intersection n2 integers
'''


n1 = int(input())
english = set(map(int, input().split()))

n2 = int(input())
french = set(map(int, input().split()))

two_subscription = english.intersection(french)

print(len(two_subscription))