def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    letters = {}
    for i in range(len(s)):
        if s[i] in letters:
            if letters[s[i]] != t[i]:
                return False
        else:
            letters[s[i]] = t[i]

    return len(letters.values()) == len(set(letters.values()))

# Another solution
def is_isomorphic_v2(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
