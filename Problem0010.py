'''
-> Task0010:
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
'''
if __name__ == '__main__':
    names = []
    scores = []
    N = int(input())
    for _ in range(N):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        students.append(stu)
    s = set(scores[:])
    second_low = list(s)[1]
    names = []
    for i in range(len(score)):
        if second_low == i[1]:
            names.append(i[0])
    names.sort()
    for name in names:
        print(name)
