'''
->Task0024:
You are given the shape of the array in the form of space-separated integers,
each integer representing the size of different dimensions,
your task is to print an array of the given shape and
integer type using the tools numpy.zeros and numpy.ones.
'''
import numpy as np
N, M, K = tuple(map(int, input().split()))
zeros = np.zeros((N, M, K), dtype = np.int8)
ones = np.ones((N, M, K), dtype = np.int8)
print(zeros)
print(ones)
