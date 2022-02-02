"""
A Max-Heap is a complete binary tree in which the value in each internal node
is bigger than or equal to the values in the children of that node.
"""


class MaxHeap:
    data: list
    size: int

    def __init__(self):
        self.data = []
        self.size = 0

    # O(log(N))
    def insert(self, dataval):
        self.data.append(dataval)
        self.size += 1
        self.sift_up(self.size-1)

    # O(log(N))
    # delete an arbitrary node index
    def delete(self, i):
        print(f"Deleting value {self.data[i]} with index {i}")
        if i >= self.size:
            raise Exception(f"Invalid delete index: {i}")
        self.data[i] = self.data[-1]
        self.data.pop()
        self.size -= 1
        self.sift_down(i)

    def delete_max(self):
        self.data[0] = self.data[-1]
        self.data.pop()
        self.size -= 1
        self.sift_down(0)

    def is_leaf(self, index):
        return index >= self.size // 2

    def get_parent(self, i):
        return (i - 1) // 2

    def get_left_child(self, i):
        return (2 * i + 1) if i <= (self.size-1) / 2 else -1

    def get_right_child(self, i):
        position = 2 * i + 2
        return position if position < len(self.data) else -1

    def sift_up(self, i):
        while i > 0:
            if self.data[i] > self.data[self.get_parent(i)]:
                self.swap(i, self.get_parent(i))
                i = self.get_parent(i)
            else:
                break

    def sift_down(self, i):
        while i <= (self.size - 1) // 2:
            if self.is_leaf(i):
                break
            lc = self.get_left_child(i)
            rc = self.get_right_child(i)
            if self.data[lc] > self.data[rc] or rc == -1:
                max_child = lc
            else:
                max_child = rc
            if self.data[i] < self.data[max_child]:
                self.swap(i, max_child)
                i = max_child
            else:
                break

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    # O(N)
    def heapify(self, val_list):
        """
        Heapify is process of creating a Heap from a Binary Tree.
        Input Example: [3, 9, 2, 1, 4, 5]
        Output Example: [9, 4, 5, 1, 3, 2]

        This algorithm just need to look the non leaf nodes.
        """
        print(f"Initial Tree: {val_list}")
        self.data = val_list
        self.size = len(val_list)
        last_parent = self.size // 2
        for i in range(last_parent, -1, -1):
            self.sift_down(i)
        print(f"Heap Tree: {self.data}")

    def print_heap(self):
        print(self.data)


heap = MaxHeap()
heap.insert(3)
heap.insert(9)
heap.insert(2)
heap.insert(1)
heap.insert(4)
heap.insert(5)
heap.print_heap()

for i in range(heap.size):
    print(heap.is_leaf(i))

print(f"For node with index 2: Parent:{heap.get_parent(2)} / {heap.data[heap.get_parent(2)]}, "
      f"Left: {heap.get_left_child(2)} / {heap.data[heap.get_left_child(2)]}, "
      f"Right: {heap.get_right_child(2)}")

heap.delete_max()
heap.print_heap()

heap.delete(1)
heap.print_heap()

heap.heapify([50, 70, 30, 1, 100, 40, 45, 3])
