'''
->TASK0044:

EXAMPLE:
AABCAAADA
3

output:
AB
CA
AD
'''

def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in range(0,n,k):
        tmp = ''
        for ch in string[i:i+k]:
            if ch not in tmp:
                tmp += ch
        print(tmp)
        
    
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)