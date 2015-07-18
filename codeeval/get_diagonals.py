# TLabs
# Get diagonals of a given matrix going from left to right

def get_diagonals(matrix):
    diagonals = []
    for row in range(2 * len(matrix) - 1):
        subdiag = []
        column = 0
        while column <= row:
            if 0 <= column < len(matrix) and 0 <= row - column < len(matrix):
                subdiag.append(matrix[row - column][column])
            column += 1
        diagonals.append(subdiag)
    return diagonals


print(get_diagonals([
  [1,2,3],
  [4,5,6],
  [7,8,9],
]))
