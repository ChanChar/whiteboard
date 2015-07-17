# Reverse Bsearch Game:
# find out what edge cases you're missing. An empty array is one for sure.

test = '100 Lower Lower Higher Lower Lower Lower Yay!'
# test = '948 Higher Lower Yay!'

def reverse_bsearch(finish, commands):
    values = [val for val in test.strip().split()]
    start, finish, commands = 0, int(values[0]), values[1:]

    for command in commands:
        if command == 'Lower':
            finish = (start + finish) / 2 - 1
        elif command == 'Higher':
            start = (start + finish) / 2 + 1
        else:
            print(round((start + finish) / 2))
