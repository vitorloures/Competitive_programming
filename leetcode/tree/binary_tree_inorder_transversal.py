# Leetcode: Binary Tree Inorder Transversal (Easy)

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + \
            self.inorderTraversal(root.right)


sol = Solution()
input_1 = TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3)))
assert sol.inorderTraversal(root=input_1) == [1, 3, 2]
assert sol.inorderTraversal(None) == []
