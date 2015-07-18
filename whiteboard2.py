# import sys
# test_cases = open(sys.argv[1], 'r')
# for test in test_cases:
#
#     print(detect_cycle(test))
# test_cases.close()


def detect_cycle(test):
    numbers = [num for num in test.strip().split()]
    endpoint = 1

    if len(numbers) <= 1:
        return ''

    pattern = []

    while endpoint != len(numbers) - 1:
        for i, num in enumerate(numbers[0:endpoint]):
            if num == numbers[endpoint]:
                if i == endpoint - 1:
                    return num
                for y in range(1, endpoint):
                    if numbers[i + y] == numbers[endpoint + y] and (i + y < endpoint):
                        if len(pattern) < 1:
                            pattern.append(num)
                        pattern.append(numbers[i + y])
        endpoint += 1
        if pattern:
            return " ".join(pattern)

    return " ".join(pattern)

# test = '2 0 6 3 1 6 3 1 6 3 1'
# test2 = '3 4 8 0 11 9 7 2 5 6 10 1 49 49 49 49'
# test3 = '1 2 3 1 2 3'
# print(detect_cycle(test))
# print(detect_cycle(test2))
# print(detect_cycle(test3))


def print_words(sentence):

    words = []
    subword = ''
    for char in sentence:
        if char.isalpha():
            subword += char.lower()
        else:
            if len(subword) > 0:
                words.append(subword)
                subword = ''
    return ' '.join(words)

print(print_words('(--9Hello----World...--)'))
print(print_words('13What213are;11you-123+138doing7'))
