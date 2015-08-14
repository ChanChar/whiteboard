def find_highest_score(test):
    rows = [[int(num) for num in row.split()] for row in test.split('|')]
    maxes = []
    for i in range(len(rows[0])):
        _max = None
        for j in range(len(rows)):
            if _max is None:
                _max = rows[j][i]
            elif rows[j][i] > _max:
                _max = rows[j][i]

        maxes.append(str(_max))

    return " ".join(maxes)

test_cases = [
"72 64 150 | 100 18 33 | 13 250 -6",
"10 25 -30 44 | 5 16 70 8 | 13 1 31 12",
"100 6 300 20 10 | 5 200 6 9 500 | 1 10 3 400 143",
]

for test in test_cases:
    print(find_highest_score(test))
