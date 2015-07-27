import math
def matrix_rotation(test):
    values = test.strip().split()
    row_length = int(math.sqrt(len(values)))
    rotated = []
    for i in range(1, row_length + 1)[::-1]:
        current = i
        for j in range(row_length):
            rotated.append(values[current * -1])
            current += row_length

    return ' '.join(rotated)
