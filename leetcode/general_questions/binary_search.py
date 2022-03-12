# Binary Search Algorithm (Easy)

from typing import List


def binarySearch(array: List, target: int) -> int:
    # Write your code here.
    start = 0
    end = len(array) - 1
    i = len(array) // 2
    while start <= i <= end:
        if array[i] == target:
            return i
        elif array[i] < target:
            start = i + 1
        else:
            end = i - 1
        i = (end - start) // 2 + start
    return -1


test_array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
test_target = 33
assert binarySearch(test_array, test_target) == 3
