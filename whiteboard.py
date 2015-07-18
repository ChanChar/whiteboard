# # Reverse Bsearch Game:
# # find out what edge cases you're missing. An empty array is one for sure.
#
# test = '100 Lower Lower Higher Lower Lower Lower Yay!'
# # test = '948 Higher Lower Yay!'
#
# def reverse_bsearch(finish, commands):
#     values = [val for val in test.strip().split()]
#     start, finish, commands = 0, int(values[0]), values[1:]
#
#     for command in commands:
#         if command == 'Lower':
#             finish = (start + finish) / 2 - 1
#         elif command == 'Higher':
#             start = (start + finish) / 2 + 1
#         else:
#             print(round((start + finish) / 2))
from collections import defaultdict
import string
def panagram(sentence):
    alphabet = { letter: 1 for letter in string.ascii_lowercase }
    for letter in sentence:
        if letter.lower() in alphabet:
            del alphabet[letter.lower()]

    remaining = "".join([letter for letter in string.ascii_lowercase if letter in alphabet])
    return remaining if len(remaining) > 0 else 'NULL'

# print(panagram('aLphabetL'))


def jolly(arr):
    numbers = [int(num) for num in arr.strip().split()]
    digits = set()
    for i, num in enumerate(numbers[1:]):
        if abs(num - numbers[i]) > 0:
            digits.add(abs(num - numbers[i]))

    expected = numbers[0] * (numbers[0] - 1) // 2
    actual = sum(digits)
    return 'Jolly' if expected == actual else 'Not Jolly'


print(jolly('9 8 9 7 10 6 12 17 24 38'))
print(jolly('3 7 7 8'))
print(jolly('4 1 4 2 3'))
