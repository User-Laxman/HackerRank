'''
->Task0005
The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i^2.

'''

if __name__ == '__main__':
    n = int(input())
    if n>=1 and n<=20:
        for i in range(n):
            print(i**2)