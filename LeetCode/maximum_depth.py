# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

def max_depth(root, depth=0):
    if root is None:
        return depth
    else:
        return max(max_depth(root.left, depth + 1), max_depth(root.right, depth + 1))
