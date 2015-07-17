# O(n) time. Checks for all chars. No edge cases?
def valid_parens(test):
    chars = []
    patterns = { '(': ')', '[': ']', '{': '}' }
    for char in list(test):
        if char in '([{':
            chars.append(char)
        else:
            try:
                if patterns[chars.pop()] != char:
                    return False
            except IndexError:
                return False

    return len(chars) == 0

test = '[]()[]([)]'

print(valid_parens(test))
