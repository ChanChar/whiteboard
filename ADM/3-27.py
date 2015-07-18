# Determine if a linked list has a loop

def find_loop(node):

    slow, fast = node, node.next()

    while fast is not None or slow != fast:
        slow = slow.next()
        for i in range(2):
            fast = fast.next()

    if fast is None:
        return 'No loops!'
    else:
        fast = node
        while fast != slow:
            fast = fast.next()
            slow = slow.next()

        return slow
    
