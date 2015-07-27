def clean_up_the_words(test):
    words = []
    word = ''
    for char in test:
        if char.isalpha():
            word += char
        else:
            if len(word) > 0:
                words.append(word)
            word = ''

    if len(word) > 0:
        words.append(word)

    return ' '.join([word.lower() for word in words])


tests = [
"(--9Hello----World...--)",
"Can 0$9 ---you~",
"13What213are;11you-123+138doing7now"]

for test in tests:
    print(clean_up_the_words(test))
