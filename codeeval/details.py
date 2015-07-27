def details(test):
    matrix = test.strip().split(',')

    distance = len(matrix[0])
    for row in matrix:
        last_x, first_y = 0, len(row)
        for i in range(len(row)):
            if row[i] == 'X':
                last_x = i
            elif row[i] == 'Y' and i < first_y:
                first_y = i

        if first_y - last_x - 1 < distance:
            distance = first_y - last_x - 1
    return distance
