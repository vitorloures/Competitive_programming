# Leetcode: Convert Sorted Array to Binary Search Tree (Medium)

from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        median = int((len(nums)-1) / 2)
        if median == 0:
            left = None
        else:
            left = self.sortedArrayToBST(nums[:median])
        if median + 1 < len(nums):
            right = self.sortedArrayToBST(nums[median+1:])
        else:
            right = None
        return TreeNode(nums[median], left, right)

sol = Solution()
sol.sortedArrayToBST([-10, -3, 0, 5, 9])


# Using DFS Technique Solution
class Solution:
    def dfs(self, nums, i, j):
        if i > j:
            return None
        mid = (i + j) // 2
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, i, mid - 1)
        root.right = self.dfs(nums, mid + 1, j)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(nums, 0, len(nums) - 1)