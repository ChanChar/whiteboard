from static_array import StaticArray

class RingBuffer:
    def __init__(self):
        self.store = StaticArray(8)
        self.capacity, self.start, self.length = 8, 0, 0

    def __getitem__(self, index):
        self.__check_index(index)
        return self.store[(self.start + index) % self.capacity]

    def __setitem__(self, index, val):
        self.__check_index(index)
        self.store[(self.start + index) % self.capacity] = val

    def __repr__(self):
        return self.store

    def __len__(self):
        return len(self.store)

    def __str__(self):
        return "{}".format(self.store)

    def pop(self):
        if self.length == 0:
            raise IndexError("Can't pop from an empty list!")
        val = self[self.length - 1]
        self[self.length-1] = None
        self.length -= 1
        self.__check_capacity()
        return val

    def append(self, val):
        self.__check_capacity()
        self[self.length] = val
        self.length += 1

    def shift(self):
        val, self[0] = self[0], None
        self.start = (self.start + 1) % self.capacity
        self.length -= 1
        self.__check_capacity()
        return val

    def unshift(self, val):
        self.__check_capacity()
        self.start = (self.start - 1) % self.capacity
        self[0] = val
        self.length += 1

    def __check_index(self, index):
        if 0 > index > self.length:
            raise IndexError("Index out of range!")

    def __check_capacity(self):
        if self.length <= (self.capacity // 2) and self.capacity > 8:
            self.__resize(False)

        if self.length == self.capacity:
            self.__resize()

    def __resize(self, up=True):
        if up:
            new_capacity = self.capacity * 2
        else:
            new_capacity = self.capacity // 2
        new_store = StaticArray(new_capacity)
        for i in range(self.length):
            new_store[i] = self[i]
        self.capacity, self.store, self.start = new_capacity, new_store, 0
