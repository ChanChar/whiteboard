from ring_buffer import RingBuffer

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
