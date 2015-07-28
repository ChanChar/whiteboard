class LinkNode:
    def __init__(self, val, prev=None, _next=None):
        self.val, self.prev, self.next = val, prev, _next

    def free_node(self):
        return self.prev is None and self.next is None

    def add_right(self, link):
        if not link.free_node():
            return 'Link is a free node!'

        if isinstance(link, LinkNode):
            self.right = link
        else:
            new_link = LinkNode(link)
            self.right = new_link

    def add_left(self, link):
        if not link.free_node():
            return 'Link is a free node!'

        if isinstance(link, LinkNode):
            self.left = link
        else:
            new_link = LinkNode(link)
            self.left = new_link

    def remove(self):
        self.prev.next, self.next.prev = self.next, self.prev
        self.next, self.prev = None, None


class SentinelLink(LinkNode):

    def __init__(self, side):
        if side not in ['first', 'last']:
            raise SideError()
        self.side = side
        self.next, self.prev = None, None

    def value(self):
        raise NotImplementedError("Sentinel nodes have no value.")

    def remove(self):
        raise NotImplementedError("Sentinel nodes can not be removed.")

    def add_right(self, link):
        if self.val != 'first':
            raise NotImplementedError("Can not add link in that direction.")
        self.next = link

    def add_left(self, val):
        if self.val != 'last':
            raise NotImplementedError("Can not add link in that direction.")
        self.prev = link
