from ring_buffer import RingBuffer
from stack import MinMaxStack

class Queue:
    def __init__(self):
        self.queue = RingBuffer()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.shift()

    def __str__(self):
        return self.queue

    def __len__(self):
        return len(self.queue)

class MinMaxStackQueue:
    def __init__(self):
        self.incoming, self.outgoing = MinMaxStack(), MinMaxStack()

    def enqueue(self, value):
        self.incoming.append(value)

    # O(1) amortized
    def dequeue(self):
        if len(self.outgoing) == 0 and len(self.incoming) == 0:
            return 'No more items to dequeue!'

        if len(self.outgoing) == 0:
            self.process_stacks()

        return self.outgoing.pop()

    def process_stacks(self):
        for i in range(len(self.incoming)):
            self.outgoing.append(self.incoming.pop())

    def current_max(self):
        if len(self.incoming) > 0 and len(self.outgoing) > 0:
            return max(self.incoming.current_max(), self.outgoing.current_max())
        elif len(self.incoming) > 0:
            return self.incoming.current_max()
        elif len(self.outgoing) > 0:
            return self.outgoing.current_max()
        else:
            return 'No items in the queue!'

    def current_min(self):
        if len(self.incoming) > 0 and len(self.outgoing) > 0:
            return min(self.incoming.current_min(), self.outgoing.current_min())
        elif len(self.incoming) > 0:
            return self.incoming.current_min()
        elif len(self.outgoing) > 0:
            return self.outgoing.current_min()
        else:
            return 'No items in the queue!'
