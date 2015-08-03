# Write a program to find the node at which the intersection of two singly linked lists begins.

def find_intersection(headA, headB):
    size1, size2 = find_length(headA), find_length(headB)
    current1, current2 = headA, headB
    if size1 > size2:
        for i in range(size1 - size2):
            current1 = current1.next
    elif size2 > size1:
        for i in range(size2 - size1):
            current2 = current2.next

    while current1 != current2 or current1 is None:
        current1 = current1.next
        current2 = current2.next

    return current1

def find_length(head):
    current = head
    size = 1
    while current.next:
        current = current.next
        size += 1
