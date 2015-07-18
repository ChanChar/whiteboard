# Singly Linked; O(n) space and time
def kth_last(head, k):
    links = []
    current = head
    while current is not None:
        links.append(current)
        current = current.next()

    return links[len(links) - k]

# O(n) time but O(1) space
def kth_last_runner_tech(head, k):
    slow, fast = head, head

    for i in range(k):
        fast = fast.next()
    while fast is not None:
        slow = slow.next()
        fast = fast.next()

    return slow


# Questions to consider:

# Do we know the length of the list?
