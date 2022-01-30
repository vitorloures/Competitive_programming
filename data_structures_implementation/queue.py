class Queue:
    """
    FIFO Structure
    """
    data: list
    _length: int

    def __init__(self, init_queue: list = []):
        if not isinstance(init_queue, list):
            raise Exception("Init data may be a list")

        self.data = init_queue
        self._length = len(init_queue)

    def enqueue(self, element):
        self.data.append(element)
        self._length += 1

    def dequeue(self):
        if self._length == 0:
            raise Exception("Queue already empty")
        out_element = self.data[0]
        self.data = self.data[1:]
        self._length -= 1
        return out_element

    def length(self):
        return self._length


########### Test set #################

import pytest


class Test:

    def test_empty_initialization(self) -> None:
        test_queue = Queue()
        assert test_queue.data == []
        assert test_queue.length() == 0

    def test_value_initialization(self) -> None:
        test_queue = Queue([7, 3, 2, 4, -1])
        assert test_queue.data == [7, 3, 2, 4, -1]
        assert test_queue.length() == 5

    def test_wrong_value_initialization(self) -> None:
        with pytest.raises(Exception):
            Queue(7)

    def test_pop_empty_queue(self) -> None:
        test_queue = Queue()
        with pytest.raises(Exception):
            test_queue.dequeue()

    def test_queue_and_dequeue(self) -> None:
        test_queue = Queue()
        test_queue.enqueue(7)
        test_queue.enqueue(3)
        test_queue.enqueue(2)
        test_queue.enqueue(4)
        test_queue.enqueue(-1)
        assert test_queue.data == [7, 3, 2, 4, -1]
        assert test_queue.length() == 5
        assert test_queue.dequeue() == 7
        assert test_queue.data == [3, 2, 4, -1]
        assert test_queue.length() == 4


