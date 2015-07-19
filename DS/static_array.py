class StaticArray:
    def __init__(self, length):
        self.store = [None] * length

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __len__(self):
        return sum([1 for item in self.store if item is not None])

    def __iter__(self):
        return self.store.iter()

    def __contains__(self, val):
        return val in self.store

    def __repr__(self):
        return self.store

    def __str__(self):
        return "{}".format(self.store)
