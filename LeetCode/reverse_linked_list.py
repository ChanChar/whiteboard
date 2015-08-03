# Reverse a singly linked list.

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverse_list(head):
    current, _next = head, None
    while current:
        temp = current.next
        current.next = _next
        _next = current
        current = temp

    return _next
