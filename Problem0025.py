'''
->Task0025:
Your task is to print an array of size N X M with its main diagonal elements as 1's and 0's everywhere else.

Note:
In order to get alignment correct, please insert the line
np.set_printoptions(legacy = '1.13')
below the numpy import.

'''

import numpy as np
np.set_printoptions(legacy = '1.13')
N, M = tuple(map(int, input().split()))
identity_mat = np.eye(N, M, k = 0)
print(identity_mat)
