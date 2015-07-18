import string

DIRS = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
LETTERS = { letter: index+1 for index, letter in enumerate(string.ascii_lowercase) }
LOWERCASE = list(string.ascii_lowercase)
def knight_moves(pos):
    x, y = list(pos)
    valid_positions = []
    for d in DIRS:
        dx, dy = d[0], d[1]
        if valid_move(LETTERS[x], int(y), dx, dy):
            valid_position = [LOWERCASE[LETTERS[x] + dx - 1], str(int(y) + dy)]
            valid_positions.append(valid_position)

    ordered_positions = sorted([''.join(pos) for pos in valid_positions])
    return ' '.join(ordered_positions)

def valid_move(x, y, dx, dy):
    checks = [x+dx > 0, x+dx < 9, y+dy > 0, y+dy < 9]
    return all(checks)

print(knight_moves('g2'))
