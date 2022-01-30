from typing import Any, Optional
from abc import ABC, abstractmethod


class SingleNode:
    data: Any
    node: Any

    def __init__(self, node_value):
        self.data = node_value
        self.next = None


class DoubleNode:
    data: Any
    node: Any
    prev: Any

    def __init__(self, node_value: Any):
        self.data = node_value
        self.next = None
        self.prev = None


class AbstractLinkedList(ABC):
    head: Any

    # O(N)
    def hasElement(self, element_to_search):
        # Test search for element in tail
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == element_to_search:
                return True
            cur_node = cur_node.next
        return False

    def print_list(self):
        cur_node = self.head
        print("\nSTART")
        while cur_node is not None:
            print(f"Node {cur_node.data} ->", end=" ")
            cur_node = cur_node.next
        print("\nEND")

        @abstractmethod
        def addFirst(self):
            pass

        @abstractmethod
        def addLast(self):
            pass

        @abstractmethod
        def getFirst(self):
            pass

        @abstractmethod
        def getLast(self):
            pass

        @abstractmethod
        def removeFirst(self):
            pass

        @abstractmethod
        def removeLast(self):
            pass


class SinglyLinkedList(AbstractLinkedList):
    head: Optional[SingleNode]

    def __init__(self):
        self.head = None

    # O(1)
    def addFirst(self, element):
        new_head = SingleNode(element)
        new_head.next = self.head
        self.head = new_head

    # O(N)
    def addLast(self, element):
        last_node = SingleNode(element)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = last_node

    # O(1)
    def getFirst(self):
        return self.head.data

    # O(N)
    def getLast(self):
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        return cur_node.data

    # O(1)
    def removeFirst(self):
        head_data = self.head.data
        self.head = self.head.next
        return head_data

    # O(N)
    def removeLast(self):
        # Test List length 1
        if self.head.next is None:
            pop_element = self.head.data
            self.head = None
            return pop_element

        prev_node = self.head
        cur_node = self.head.next
        while cur_node.next is not None:
            prev_node = cur_node
            cur_node = cur_node.next

        prev_node.next = None
        return cur_node.data


class DoublyLinkedList(AbstractLinkedList):
    head: Optional[DoubleNode]

    def __init__(self):
        self.head = None

    # O(1)
    def addFirst(self, element):
        new_head = DoubleNode(element)
        new_head.next = self.head
        self.head.prev = new_head
        self.head = new_head

    # O(N)
    def addLast(self, element):
        last_node = DoubleNode(element)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = last_node
        last_node.prev = cur_node

    # O(1)
    def getFirst(self):
        return self.head.data

    # O(N)
    def getLast(self):
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        return cur_node.data

    # O(1)
    def removeFirst(self):
        head_data = self.head.data
        self.head = self.head.next
        self.head = None
        return head_data

    # O(N)
    def removeLast(self):
        # Test List length 1
        if self.head.next is None:
            pop_element = self.head.data
            self.head = None
            return pop_element

        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next

        pop_element = cur_node.data
        new_last_node = cur_node.prev
        new_last_node.next = None
        return pop_element


# Naive and non automatic test set


sll = SinglyLinkedList()
sll.addFirst(7)
sll.addFirst(3)
sll.addFirst(2)
sll.print_list()
sll.addLast(4)
sll.addLast(-1)
sll.print_list()
print(f"Has 4: {sll.hasElement(4)}", end=" ")
print(f"Has 10: {sll.hasElement(10)}", end=" ")
sll.removeFirst()
sll.removeLast()
sll.print_list()

