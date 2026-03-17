'''
->Task017:
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.
For Ex:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

'''

def swap_case(s):
    s_len = len(s)
    modified_string = str()
    for i in range(s_len):
        if s[i].isupper():
            modified_string += s[i].lower()
        elif s[i].islower():
            modified_string += s[i].upper()
        else:
            modified_string += s[i]                
    return modified_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
