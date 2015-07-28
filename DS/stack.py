from dynamic_array import DynamicArray

class Stack(DynamicArray):

    def shift(self):
        raise NotImplementedError("Can't shift into a stack!")

    def unshift(self):
        raise NotImplementedError("Can't unshift into a stack!")

    def __getitem__(self):
        raise NotImplementedError("Can't index into a stack! Try peek instead.")

    def __setitem__(self):
        raise NotImplementedError("Can't set items in a stack!")

    def peek(self):
        return self.store[-1]

class MinMaxStack:

    def __init__(self):
        # Made it easier for myself. :[
        self.store = []

    def append(self, value):
        if len(self.store) == 0:
            # where [value, current min, current max]
            self.store.append([value, value, value])
        else:
            current_min = min([self.store[-1][1], value])
            current_max = max([self.store[-1][2], value])
            self.store.append([value, current_min, current_max])

    def pop(self):
        return self.store[-1][0]

    def current_min(self):
        return self.store[-1][1]

    def current_max(self):
        return self.store[-1][2]
