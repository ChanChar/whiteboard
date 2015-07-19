from static_array import StaticArray

class DynamicArray:
    def __init__(self):
        self.store, self.capacity, self.length = StaticArray(8), 8, 0

    def __getitem__(self, index):
        self.__check_index(index)
        return self.store[index]

    def __setitem__(self, index, val):
        self.__check_index(index)
        self.store[index] = val

    def __repr__(self):
        return self.store

    def __len__(self):
        return len(self.store)

    def __str__(self):
        return "{}".format(self.store)

    def pop(self):
        if self.length == 0:
            raise IndexError("Can't pop from an empty list!")
        val = self.store[self.length - 1]
        self.store[self.length-1] = None
        self.length -= 1
        self.__check_capacity()
        return val

    def push(self, val):
        self.__check_capacity()
        self.store[self.length] = val
        self.length += 1

    def shift(self):
        val = self.store[0]
        for i in range(1, self.length):
            self.store[i - 1] = self.store[i]
        self.store[self.length - 1] = None
        self.length -= 1
        self.__check_capacity()
        return val

    def unshift(self, val):
        self.__check_capacity()
        i = self.length
        while i > 0:
            self.store[i] = self.store[i-1]
            i -= 1
        self.store[0] = val
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
            new_store[i] = self.store[i]
        self.capacity, self.store = new_capacity, new_store
