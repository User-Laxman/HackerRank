'''
->TASK0041:

size = 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

'''

# ord('A') for char to ascii number of it
# chr(65) for number to ascii character of it
# A = 65, a = 97
def print_rangoli(size):
    # your code goes here
    width = size*2 - 1 + size*2 - 2
    n = size * 2 -1
    j = size
    lst = []
    for i in range(n):
        if i > size-1:
            prefix = [chr(96+x) for x in range(j,1+(i%j), -1)]
            suffix = prefix[:-1]
            lst = prefix+suffix[::-1]
        else:
            prefix = [chr(96+x) for x in range(j,j-i-1, -1)]
            suffix = prefix[:-1]
            lst = prefix+suffix[::-1]
        string = '-'.join(lst)
        print(string.center(width, '-'))
        
        
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)