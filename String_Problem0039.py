'''
->TASK0039:
Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

sample design: with i/p's: n = 9, m = 21

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

'''

n, m = tuple(map(int, input().split()))

center = n //2 + 1

for i in range(1, n, 2):
    string = ('.|.'*i).center(m, '-')
    print(string)
    
print('WELCOME'.center(m, '-'))

for i in range(n-2, 0, -2):
    string = ('.|.'*i).center(m, '-')
    print(string)
