# Max Howell: Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.

from collections import deque
def invertTree(root):
    if root is None:
        return root
    bf_stack = deque([root])
    while bf_stack:
        current = bf_stack.popleft()
        if current.left:
            bf_stack.append(current.left)
        if current.right:
            bf_stack.append(current.right)

        current.left, current.right = current.right, current.left

    return root

# Since there is no need to search left to right a simple stack will also suffice.
def invertTree_v2(root):
    if root is None:
        return root

    stack = [root]
    while stack:
        current = stack.pop()
        if current is not None:
            stack.append(current.left)
            stack.append(current.right)

    return root
