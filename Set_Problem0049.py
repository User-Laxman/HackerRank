'''
-->TASK0049:
INPUT:
1st line: n - no.of elements in set 's'
2nd: n space separated values
3rd: integer N, next N commands
4th: N commands such as remove, pop or discard

OUPTUT: remained elements
'''
from collections import deque
n = int(input())
s = set(map(int, input().split()))

N = int(input())
queue = deque()

for i in range(N):
    queue.append(input())

for i in range(N):
    command = queue.popleft()
    if command == 'pop':
        s.pop()
    elif command[0] == 'r':
        if int(command[-1]) in list(s):
            s.remove(int(command[-1]))
    elif command[0] == 'd':
        s.discard(int(command[-1]))

print(sum(list(s)))    
    
    
