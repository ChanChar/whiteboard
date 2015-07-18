# No temp buffer; O(n^2)
def remove_dups(head):
    current, runner = head, head.next

    while runner is not None:
        if runner.val() == current.val()
            old, runner = runner, runner.next
            old.remove()
        else:
            runner = runner.next

        if runner is None:
            current = current.next
            runner = current.next

    return 'Dups Removed'

# O(n)
def remove_dups_with_buffer(head):
    seen = set()
    current = head
    while current is not None:
        if current in seen:
            old = current
            current = current.next()
            old.remove()
        else:
            seen.add(current)
            current = current.next()
