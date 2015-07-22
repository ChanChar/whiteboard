from link_node import LinkNode, SentinelLink

class LinkedList:
    def __init__(self):
        self.first = SentinelLink('first')
        self.last = SentinelLink('Last')
