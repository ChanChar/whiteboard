# Reverse the words in a sentence.
def reverse_sentence(sentence):
    words = [word for word in sentence.split()]
    for i in range(len(words) // 2):
        words[i], words[len(words) - i - 1] = words[len(words) - i - 1], words[i]
    return " ".join(words)

def pythonic_reverse(sentence):
    words = [word for word in sentence.split()]
    return " ".join(words[::-1])

print(reverse_sentence('My name is Chris'))
print(pythonic_reverse('My name is Chris'))
