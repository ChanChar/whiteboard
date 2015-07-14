# Find the overhead fraction (the ratio of data space over total space) for each of the binary implementations.

# a. All nodes store data, two child pointers, and a parent pointer. Data field requires 4 bytes and each pointer 4 bytes.
# b. Only leaf nodes store data, internal nodes store two child pointers. The data field requires 4 bytes,
# and each pointer requires 2 bytes.

# Notes: deques in python are implemented as doubly linked lists and are awesome for queues.

# a

from collections import deque

# 4 / (4 + 3 * 4) = 1/4 Ratio of data over total space

def calculate_data(head):
    total_data = 0
    nodes = deque(head)

    while len(nodes):
        current = nodes.popleft()

        total_data += 4
        if current.parent():
            total_data += 4

        for child in current.children():
            nodes.append(child)
            total_data += 4

    return total_data

# b

# 4 * n / (4 * n + 4*(n-1)) = n / 2 * n - 1 
def calculate_data_v2(head):
    total_data = 0
    nodes = deque(head)

    while len(nodes):
        current = nodes.popleft()

        if current.parent() and current.children():
            for child in current.children():
                nodes.append(child)
                total_data += 2
        elif len(current.children()) == 0:
            total_data += 4
