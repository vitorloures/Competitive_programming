# Leetcode: Binary Tree Level Order Traversal (Medium)

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cur_level = []
        solution = []
        if root is None:
            return []
        cur_level.append(root)
        while len(cur_level) != 0:
            solution.append([node.val for node in cur_level])
            next_level = []
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level

        return solution


import collections

# An easier to understand solution
class Solution2:
    def levelOrder(self, root):
        result = []
        if not root:
            return result
        queue = collections.deque()
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result