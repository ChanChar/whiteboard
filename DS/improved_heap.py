from heap import MinHeap

class ImprovedHeap(MinHeap):

    # use the array representation to swap and a hashmap to keep and update tracks as changes occur

    # Hashmap method (for dense):
    #      - Shift: O(n)
    #      - Insert: O(1)
    #
    # Heap + Hashmap method (for sparse):
    #      - Shift: O(logn)
    #      - Insert: O(logn)
