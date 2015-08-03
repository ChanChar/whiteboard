# from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(30)
node1, node2, node3, node4, node5, node6 = Node(8), Node(52), Node(3), Node(20), Node(10), Node(29)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node4.left = node5
node4.right = node6

# v1. Where lowest common ancestor can not be the given node itself.
# def find_lc_ancestor(node1, node2):
#     queue = deque()
#     queue.append(root)
#     while len(queue) > 0:
#         current = queue.popleft()
#         if any([True for ch in current.children if (ch.value in [node1, node2])]):
#             return current.value
#         else:
#             for ch in current.children:
#                 queue.append(ch)
#
#     return None


def find_lc_ancestor(root, p, q):
    current = root
    while True:
        if p <= current.val <= q or p >= current.val >= q:
            return current.val
        elif p < current.val and q < current.val:
            current = current.left
        elif p > current.val and q > current.val:
            current = current.right
        else:
            return None

print(find_lc_ancestor(root, 8, 52))
