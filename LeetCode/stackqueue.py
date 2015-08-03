# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.

# Notes:
# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

class Stack:
    def __init__(self):
        self.store = []

    def push(self, val):
        self.store.append(val)

    def pop(self):
        return self.store.pop()

    def empty(self):
        return len(self.store) == 0

    def peek(self):
        return self.store[-1]

    def size(self):
        return len(self.store) - 1


class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.incoming = Stack()
        self.outgoing = Stack()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.incoming.push(x)

    # @return nothing
    def pop(self):
        self.process_stacks()
        if not self.outgoing.empty():
            self.outgoing.pop()

    # @return an integer
    def peek(self):
        self.process_stacks()
        if not self.outgoing.empty():
            return self.outgoing.peek()

    # @return an boolean
    def empty(self):
        return self.outgoing.empty() and self.incoming.empty()

    def process_stacks(self):
        if self.outgoing.empty():
            while not self.incoming.empty():
                self.outgoing.push(self.incoming.pop())
