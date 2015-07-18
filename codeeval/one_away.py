# CTCI: Given two strings, write a function to check if they are one edit (or zero edits) away.
from collections import defaultdict

def one_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    letters = defaultdict(int)
    for letter in list(str1):
        letters[letter] += 1

    diff = 0

    for letter in list(str2):
        if letter not in letters:
            diff += 1
        else:
            letters[letter] -= 1

    return True if (0 <= diff <= 1) else False
