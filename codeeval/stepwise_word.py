def longest_word(words):
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

def stepwise_word(word):
    stepwise_parts = []
    for i, char in enumerate(list(word)):
        stepwise_parts.append((i * '*' + char))

    return " ".join(stepwise_parts)

words = ['hello', 'cat', 'dog']

longest = longest_word(words)
print(stepwise_word(longest))
