'''
->TASK0036:
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

'''

def count_substring(string, sub_string):
    pos = string.find(sub_string[0])
    m = len(string)
    n = len(sub_string)
    count = 0
    if m >= n:
        for i in range(m-n + 1):
            if string[i:i+n] == sub_string:
                count += 1  
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)