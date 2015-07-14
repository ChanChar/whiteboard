def longest_word(words):
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

def stepwise_word(word):
    stepwise = ''
    for i, char in enumerate(list(word)):
        if i == 0:
            stepwise += (i * '*' + char)
        else:
            stepwise += (" " + i * '*' + char)

    return stepwise

words = ['hello', 'cat', 'dog']

longest = longest_word(words)
print(stepwise_word(longest))
