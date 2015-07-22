class SideError(Exception):
    pass

class LinkNode:
    def __init__(self, val, prev=None, _next=None):
        self.val, self.prev, self.next = val, prev, _next

    def free_node(self):
        return self.prev is None and self.next is None

    def add_right(self, link):
        if not link.free_node():
            raise Exception('')

    def add_left(self, link):


    def remove(self):
        self.prev.next, self.next.prev = self.next, self.prev
        self.next, self.prev = None, None

class SentinelLink(LinkNode):

    def __init__(self, side):
        if side not in ['first', 'last']:
            raise SideError()
        self.side = side

    def value(self):
        raise NotImplementedError("Sentinel nodes have no value.")

    def remove(self):
        raise NotImplementedError("Sentinel nodes can not be removed.")

    def add_right(self, link):
        if self.val != 'first':
            raise NotImplementedError("Can not add link in that direction.")

        self.



    def add_left(self, val):
