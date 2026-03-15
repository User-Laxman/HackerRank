'''
-> Task0016:
Neo has a complex matrix script. The matrix script is a N X M grid of strings.
It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

To decode the script,
Neo needs to read each column and
select only the alphanumeric characters and connect them.
Neo reads the column from top to bottom and
starts reading from the leftmost column.
If there are symbols or spaces between
two alphanumeric characters of the decoded script,
then Neo replaces them with a single space '' for better readability.
Neo feels that there is no need to use 'if' conditions for decoding.
Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

The first line contains space-separated integers N (rows) and M (columns) respectively.
The next N lines contain the row elements of the matrix script.
'''


import re

def find_replace(pattern, st):
    matches = re.findall(pattern, st)
    for match in matches:
        length = len(match)
        st = st.replace(match[1:length-1], ' ')
    return st

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
st1 = ""

for j in range(len(matrix[0])):
    for i in matrix:
        st1 += i[j]
    st1 += ''
s = re.sub(r'(?<=\w)[\s\W_]+(?=\w)', ' ', st1, flags=re.ASCII)
print(s)
