# Input: 3;3;1 2 3 4 5 6 7 8 9

def print_spiral(test):
    n, m, values = test.strip().split(';')
    n, m = int(n), int(m)
    spiral = []
    matrix = create_matrix(n, m, [i for i in values.split()])
    total = n * m

    while total > 0:
        for el in matrix[0]:
            spiral.append(el)
            total -= 1
        matrix = rotate(matrix[1:])[::-1]

    return spiral

def rotate(matrix):
    return [row for row in zip(*matrix)]

def create_matrix(n, m, values):
    matrix = []
    row_start = 0
    for y in range(m):
        row = []
        for x in range(n):
            row.append(values[x + row_start])
        matrix.append(row)
        row_start += n

    return matrix

print(print_spiral('3;3;1 2 3 4 5 6 7 8 9'))
