'''
-> Task0010:
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
'''
if __name__ == '__main__':
    students = [[],[]]
    N = int(input())
    for _ in range(N):
        name = input()
        score = float(input())
        students[0].append(name)
        students[1].append(score)
    s = set(students[1])
    s = list(s)
    s.sort()
    second_low = s[1]
    names = []
    for i in range(len(students[0])):
        if second_low == students[1][i]:
            names.append(students[0][i])
    names.sort()
    for name in names:
        print(name)
