'''
->Task0021:
A NumPy array is a grid of values. They are similar to lists,
except that every element of an array must be the same type.

You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.
'''


import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.sort(reverse = True)
    return np.array(arr)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
