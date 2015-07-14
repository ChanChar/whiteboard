def string_compression(word):
    if len(set(word)) * 2 > len(word):
        return word

    compressed = ""
    current, count = word[0], 1

    for letter in list(word)[1:]:
        if current == letter:
            count += 1
        else:
            compressed += (current + str(count))
            current, count = letter, 1

    return compressed + letter + str(count)
