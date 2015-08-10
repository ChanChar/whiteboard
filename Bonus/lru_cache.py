from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.history = OrderedDict()

    def get(self, key):
        if key in self.history:
            self.set(key, self.history[key])
            return self.history[key]
        else:
            return -1

    def set(self, key, value):
        if key in self.history:
            del self.history[key]
            self.history[key] = value
        else:
            if len(self.history) == self.capacity:
                self.history.popitem(False)
            self.history[key] = value
