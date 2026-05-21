'''
->Task15: Use Python 2 for submit the code, cause the python3 has different from python2 hash() and they used test cases from  
The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t
Print the result of hash(t).
'''
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print(hash(tuple(integer_list)))
