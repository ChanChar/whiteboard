# Floyd's Cycle Detection Algorithm

def detect_cycle(head):
    slow, fast = head, head
    for i in range(2):
        try:
            fast = fast.next
        except AttributeError:
            return 'No cycle detected!'

    while fast is not None or slow != fast:
        slow = slow.next
        for i in range(2):
            try:
                fast = fast.next
            except AttributeError:
                return 'No cycle detected!'

    if fast is None:
        return 'No cycle detected!'

    # Optional: Find where the cycle begins.
    fast = head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    return slow
