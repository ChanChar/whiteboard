def partition(head, val):
    first, second = LinkedList(), LinkedList()
    current = head

    while current is not None:
        if current.val() < val:
            first.add(current.val())
        else:
            second.add(current.val())
        current = current.next()

    second.head().prev() = first.last()
    first.last().next() = second.head()

    return first.head()

# Alternate solution:
# Keep track of head and tail and simply add to either end.

def partition(head, val):
    new_list = LinkedList()
    head, tail = new_list.head(), new_list.tail()

    current = head
    while current is not None:
        if current.val() < val:
            new_node = Node(val)
            head.prev() = new_node
            new_node.next() = head
            head = new_node
        else:
            new_node = Node(val)
            tail.next() = new_node
            new_node.prev() = tail
            tail = new_node

    return new_list
