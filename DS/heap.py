class MinHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def peek(self):
        if self.size() > 0:
            return self.heap[0]
        else:
            return 'Heap is empty.'

    def add(self, val):
        self.heap.append(val)
        self.heapify_up(self.heap, self.size() - 1, self.size())
        return self.heap

    def extract(self):
        if self.size() == 0:
            return 'Heap is empty.'
        temp = self.heap[0]
        if self.size() > 1:
            self.heap[0] = self.heap.pop()
            self.heapify_down(self.heap, 0, self.size())
        else:
            return self.heap.pop()

        return temp

    @staticmethod
    def get_children_indices(size, parent_index):
        pos = 2 * parent_index
        return [pos + i for i in range(1, 3) if pos + i < size]

    @staticmethod
    def get_parent_index(child_index):
        if child_index == 0:
            return "Root has no parent."
        return (child_index - 1) // 2

    def heapify_up(self, heap, child_index, size=None):
        if child_index == 0:
            return heap
        size = size or len(heap)
        parent_index = self.get_parent_index(child_index)
        child_val, parent_val = heap[child_index], heap[parent_index]

        if parent_val > child_val:
            heap[child_index], heap[parent_index] = parent_val, child_val
            self.heapify_up(heap, parent_index, size)
        else:
            return heap

    def heapify_down(self, heap, parent_index, size=None):
        size = size or len(heap)
        children_indicies = self.get_children_indices(size, parent_index)
        children = [heap[i] for i in children_indicies]
        parent_val = heap[parent_index]
        if all([child > parent_val for child in children]):
            return heap

        if len(children) < 2:
            temp = children_indicies[0]
        else:
            if children[0] > children[1]:
                temp = children_indicies[1]
            else:
                temp = children_indicies[0]

        heap[parent_index], heap[temp] = heap[temp], parent_val
        self.heapify_down(heap, parent_index, size)
