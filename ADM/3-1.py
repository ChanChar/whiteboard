def correct_parens(string):
    stack = []
    for i, paren in enumerate(list(string)):
        if paren == '(':
            stack.append(paren)
        else:
            try:
                stack.pop()
            except IndexError:
                return i

    return len(stack) == 0
