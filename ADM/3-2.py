# Questions to ask:
# Do I have the length of the list?
# Do I have pointers to the head and end of this list?

# Process:
# 1. Save current, next, and prev
# 2. While the current isn't None, we can traverse through each one swapping the direction to point at the prev.

def reverse_linked_list(head):

    current = head
    next_temp = head.next()
    prev = head

    while next_temp is not None:
        if current == head:
            current.next() = None

        current = next_temp
        next_temp = current.next()
        current.next() = prev
        prev = current

    return prev
