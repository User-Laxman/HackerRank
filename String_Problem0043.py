'''
-->TASK0043:
Understand the code of minion game,
example: stuart starts with consonants, kevin starts with vowels
BANANA
'''
def minion_game(string):
    """Calculate scores for Stuart and Kevin in O(n) time.
    Stuart scores for substrings starting with consonants, Kevin for vowels.
    """
    stuart_score = 0
    kevin_score = 0
    n = len(string)
    vowels = set('AEIOU')
    for i, ch in enumerate(string):
        if ch in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input().strip()
    minion_game(s)
