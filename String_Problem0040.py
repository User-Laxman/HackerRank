'''
->TASK0040	:

Given an integer, n, print the following values for each integer i from 1 to n:
Decimal
Octal
Hexadecimal (capitalized)
Binary


ex: 
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001

'''
def print_formatted(number):
    # your code goes here
    n = len(bin(number)[2:])+1
    for i in range(1, number+1):
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        string = str(i).rjust(n-1, ' ')+octa.rjust(n, ' ')+hexa.rjust(n, ' ')+binary.rjust(n, ' ')
        print(string)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)