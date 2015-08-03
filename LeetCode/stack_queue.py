from collections import deque
class Stack:
    def __init__(self):
        self.queue = deque()
        self.temp = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        while len(self.queue) > 1:
            self.temp.append(self.queue.popleft())

        value = self.queue.popleft()
        self.queue, self.temp = self.temp, self.queue
        return value

    def top(self):
        return self.queue[-1]
        # If indexing is not allowed use the following approach.
        # while len(self.queue) > 1:
        #     self.temp.append(self.queue.popleft())
        #
        # value = self.queue.popleft()
        # self.queue, self.temp = self.temp, self.queue
        # self.queue.append(value)
        # return value

    def empty(self):
        return len(self.queue) == 0
