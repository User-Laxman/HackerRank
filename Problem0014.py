if __name__ == '__main__':
    N = int(input())
    lst = []
    taken_lst = []
    for i in range(N):
        row = input().strip().split()
        lst.append(row)
    for row in lst:
        if row[0] == 'insert':
            taken_lst.insert(int(row[1]), int(row[2]))
        elif row[0] == 'print':
            print(taken_lst)
        elif row[0] == 'remove':
            taken_lst.remove(int(row[1]))
        elif row[0] == 'append':
            taken_lst.append(int(row[1]))
        elif row[0] == 'sort':
            taken_lst.sort()
        elif row[0] == 'pop':
            taken_lst.pop()
        elif row[0] == 'reverse':
            taken_lst.reverse()
        else:
            pass
