# Given a search string and a magazine, determine if the magazine has the letters to compose the search string.
# O(n) worst case we have to look at all the letters in the magazine so O(n) time is needed.
from collections import defaultdict
def search_text(search, magazine):
    count, letters = 0, defaultdict(int)
    for letter in search:
        letters[letter] += 1
        count += 1

    for letter in magazine:
        if letters[letter] > 0:
            count -= 1
            letters[letter] -= 1

        if count == 0:
            return True

    return False

print(search_text('hello', 'hthis eis la lmagazine owith in it'))
