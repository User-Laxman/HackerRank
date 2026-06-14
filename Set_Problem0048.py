'''
-->TASK0048:
Input: first line, input N
suceeding lines: N lines of country names

OUTPUT: distinct countries
'''
N = int(input())
store_values = [input() for i in range(N)]
distinct_countries = set(store_values)
print(len(distinct_countries))