'''
-> TASK0036:
You are given a string.
Your task is to find out if the string  contains any: 
alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
 '''

#str.isalnum() , str.isalpha(), str.isdigit(), str.islower(), str.isupper()
if __name__ == '__main__':
    s = input()
    truths = [False, False, False, False, False]
    for i in range(len(s)):
        truths[0] = s[i].isalnum() or truths[0]
        truths[1] = s[i].isalpha() or truths[1]
        truths[2] = s[i].isdigit() or truths[2]
        truths[3] = s[i].islower() or truths[3]
        truths[4] = s[i].isupper() or truths[4]
    for truth in truths:
        print(truth)