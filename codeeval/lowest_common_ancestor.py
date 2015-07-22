from collections import deque

class Node:
    def __init__(self, value, parent=None, children=None):
        self.value = value
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

root = Node(30)
node1, node2, node3, node4, node5, node6 = Node(8), Node(52), Node(3), Node(20), Node(10), Node(29)

root.add_child(node1)
root.add_child(node2)
node1.add_child(node3)
node1.add_child(node4)
node4.add_child(node5)
node4.add_child(node6)

def find_lc_ancestor(node1, node2):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        current = queue.popleft()
        if any([True for ch in current.children if (ch.value in [node1, node2])]):
            return current.value
        else:
            for ch in current.children:
                queue.append(ch)

    return None
