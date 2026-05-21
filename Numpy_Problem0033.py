'''
->TASK0033:
You are given the coefficients of a polynomial P .
Your task is to find the value of P at point x .
'''

import numpy as np

A = np.array(list(map(float, input().split())))
x = int(input())

print(np.polyval(A,x))