# That is pretty cool.
# Note it doesn't work if the given node is the last node in the list. 
def delete_middle(node):
    current = node.next()
    node.next().delete()
    node = current
