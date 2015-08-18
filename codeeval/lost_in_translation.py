tests = [
    "rbc vjnmkf kd yxyqci na rbc zjkfoscdd ew rbc ujllmcp",
    "tc rbkso rbyr ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "de kr kd eoya kw aej icfkici re zjkr"
]

translated_tests = [
    "the public is amazed by the quickness of the juggler",
    "we think that our language is impossible to understand",
    "so it is okay if you decided to quit"
]

decoder = {'g': 'v', 'h': 'x', 'r': 't', 'l': 'g', 's': 'n', 'j': 'u', 'o': 'k', 'w': 'f', 'z': 'q', 't': 'w', 'u': 'j', 'i': 'd', 'a': 'y', ' ': ' ', 'f': 'c', 'd': 's', 'p': 'r', 'v': 'p', 'n': 'b', 'y': 'a', 'c': 'e', 'k': 'i', 'm': 'l', 'e': 'o', 'x': 'm', 'b': 'h', 'q': 'z'}

for row, test in enumerate(tests):
    for i, word in enumerate(test):
        for letter in word:
            decoder[letter] = translated_tests[row][i]

print(decoder)
a = (set(decoder.keys()))
b = (set(decoder.values()))

print (b-a)

print(a ^ b)
import string

for letter in string.ascii_lowercase:
    missing = []
    if letter not in decoder:
        missing.append(letter)

print(missing)

def translate(phrase):
    decoded = ''
    for char in phrase:
        decoded += decoder[char]

    return decoded

for test in tests:
    print(translate(test))
