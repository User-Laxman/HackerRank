''' 
->Task 0002
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

Input Format: A single line containing a positive integer, n.

Constraints: 1 <= n <= 100

 '''
if __name__ == '__main__':
    n = int(input().strip())
    even = n % 2 ==0
    if not (n >= 1 and n <= 100):
        exit(0)        
    if not even:
        print('Weird')
    if even:
        if n >= 2 and n <= 5:
            print('Not Weird')
        elif n >= 6 and n <= 20:
            print('Weird')
        else:
            print('Not Weird')
        
