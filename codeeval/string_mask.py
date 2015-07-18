def string_mask(word, binary):
    unmasked = ''
    for i, char in enumerate(list(binary)):
        if char == '1':
            unmasked += word[i].upper()
        else:
            unmasked += word[i]
    return unmasked
