'''
->TASK0038:
You are given a string s and width w.
Your task is to wrap the string into a paragraph of width w.
'''
def wrap(string, max_width):
    m = len(string)
    n = m // max_width 
    lst = []
    prev = 0
    for i in range(1, n+2):        
        lst.append(string[prev*max_width:i*max_width])
        prev = i
    return '\n'.join(lst)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)