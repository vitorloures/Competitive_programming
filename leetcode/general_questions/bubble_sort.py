# Time: Best Case O(n); Average case O(n²); Space O(1).
# n is the number og elements in the array

def bubbleSort(array):
    end = len(array)
    isSorted = False
    while not isSorted:
        isSorted = True
        for j in range(end - 1):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
                isSorted = False
        end -= 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]