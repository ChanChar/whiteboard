# Correct parens, O(N) time, O(1) space.

def solution(S):
    left = 0
    if len(S) == 0:
        return 1
    for char in S:
        if char == "(":
            left += 1
        else:
            if left > 0:
                left -= 1
            else:
                return 0
    if left == 0:
        return 1
    else:
        return 0
