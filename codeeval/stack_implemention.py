# Completed

import sys
def implement_stack(arr):
    stack = []
    reverse_stack = []
    i = 0

    for el in arr:
        stack.append(el)
    while len(stack) > 0:
        if i % 2 == 0:
            reverse_stack.append(str(stack.pop()))
        else:
            stack.pop()
        i += 1
    return " ".join(reverse_stack)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums = [int(num) for num in test.strip().split()]
    print(implement_stack(nums))

test_cases.close()
