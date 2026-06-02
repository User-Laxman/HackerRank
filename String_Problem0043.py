import re
def matches(pattern, string):
    n = len(string)
    idx = string.find(pattern[0])
    count = 0
    if len(pattern) == 1:
        return string.count(pattern)
    while True:
        if n > idx and idx != -1 and n > idx+len(pattern)-1:
            if string[idx:idx+len(pattern)] == pattern:
                count += 1
            idx += 1
        else:
            break
    return count

def minion_game(string):
    s1 = {}
    s2 = {}
    vowels = []
    consonants = []
    for ch in string:
        if re.match(r'[AEIOU]', ch):
            vowels.append(ch)
            s2[ch] = string.count(ch)
        else: 
            s1[ch] = string.count(ch)
            consonants.append(ch)
    
    for c in consonants:
        idx = string.index(c)
        for i in range(1 , len(string)-idx+1):
            word = string[idx:idx+i]
            score = matches(word, string)
            s1[word] = score

    for c in vowels:
        idx = string.index(c)
        for i in range(1 , len(string)-idx+1):
            word = string[idx:idx+i]
            score = matches(word, string)
            s2[word] = score
    sums = []

    for player in [s1,s2]:
        total = 0
        for each in player.values():
            total += each
        sums.append(total)
    if sums[0] > sums[1]:
        print("Stuart", sums[0])
    elif sums[1] > sums[0]:
        print("Kevin", sums[1])
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)