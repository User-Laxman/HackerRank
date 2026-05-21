''' 
->Task 0003
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
    1. The first line contains the sum of the two numbers.
    2. The second line contains the difference of the two numbers (first - second).
    3. The third line contains the product of the two numbers.
'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if (a >= 1 & a <=10**10) and (b >= 1 & b <=10**10):
        print(a+b)#first line
        print(a-b)#second line
        print(a*b)#third line