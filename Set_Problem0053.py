'''
TASK0053:  .symmetric_difference()
'''

english_total = int(input())
english_roll = set(list(map(int, input().split())))

french_total = int(input())
french_roll = set(list(map(int, input().split())))

both = english_roll.symmetric_difference(french_roll)

print(len(both))
