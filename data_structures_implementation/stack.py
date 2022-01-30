import typing

"""
Python built in list makes trivial to work with stacks. I'ld not be necessary 
to implement this class in algorithms problems. 
"""


class Stack:
    data: list
    _length: int

    def __init__(self, init_stack: list = []) -> None:
        if isinstance(init_stack, list):
            self.data = init_stack
            self._length = len(init_stack)
        else:
            raise Exception('Initialization values should be in a list')

    def top(self) -> typing.Any:
        return self.data[-1]

    def length(self) -> int:
        return self._length

    def pop(self) -> typing.Any:
        if self.length == 0:
            raise Exception('The stack is already empty')
        else:
            pop_element = self.data.pop()
            self._length -= 1
            return pop_element

    def stack(self, element: typing.Any) -> None:
        self.data.append(element)
        self._length += 1


import pytest


class Test:

    def test_empty_initialization(self) -> None:
        test_stack = Stack()
        assert test_stack.data == []
        assert test_stack.length() == 0

    def test_value_initialization(self) -> None:
        test_stack = Stack([7, 3, 2, 4, -1])
        assert test_stack.data == [7, 3, 2, 4, -1]
        assert test_stack.length() == 5
        assert test_stack.top() == -1

    def test_wrong_value_initialization(self) -> None:
        with pytest.raises(Exception):
            Stack(7)

    def test_pop_empty_stack(self) -> None:
        test_stack = Stack()
        with pytest.raises(Exception):
            test_stack.pop()

    def test_stack_and_pop(self) -> None:
        test_stack = Stack()
        test_stack.stack(7)
        test_stack.stack(3)
        test_stack.stack(2)
        test_stack.stack(4)
        test_stack.stack(-1)
        assert test_stack.data == [7, 3, 2, 4, -1]
        assert test_stack.length() == 5
        assert test_stack.top() == -1
        assert test_stack.pop() == -1
        assert test_stack.data == [7, 3, 2, 4]
        assert test_stack.length() == 4
