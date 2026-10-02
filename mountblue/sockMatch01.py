#!/bin/python3

import os
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    # Write your code here
    counter = {}
    sum = 0
    for i in range(n):
        if ar[i] not in counter.keys():
            counter[ar[i]] = 0
        counter[ar[i]] += 1
        if counter[ar[i]] % 2 == 0:
            sum+=1 
    return sum
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
