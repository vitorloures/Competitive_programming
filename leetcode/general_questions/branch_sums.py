# Branch Sum: Easy

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_leaf(node):
    return not node.left and not node.right


def getBranchSums(node, cur_sum, sums):
    cur_sum += node.value
    if is_leaf(node):
        sums.append(cur_sum)
        return
    if node.left:
        getBranchSums(node.left, cur_sum, sums)
    if node.right:
        getBranchSums(node.right, cur_sum, sums)
    return sums


def branchSums(root):
    sums = []
    runningSum = 0
    # This function has a side effect of appending values to sums
    getBranchSums(root, runningSum, sums)
    return sums


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTreeTest(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(branchSums(tree), [15, 16, 18, 10, 11])


class BinaryTreeTest(BinaryTree):

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self
