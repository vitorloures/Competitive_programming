# Leetcode: Symmetric Tree (Easy)

from typing import Optional, List

"""
Idea: The InOrder traversal Algorithm must return lists in reversed order, when
the Binary Tree is symmetric. We use a string to label the depth to avoid comparing 
values of different heights and generating a False Positive.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive Solution
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_inorder = self.inOrder(root.left, 1)
        right_inorder = self.inOrder(root.right, 1)

        if len(left_inorder) != len(right_inorder):
            return False
        else:
            for i in range(len(left_inorder)):
                if left_inorder[i] != right_inorder[-i-1]:
                    return False
        return True

    def inOrder(self, root: Optional[TreeNode], depth: int) -> List:
        if root is None:
            return []
        return self.inOrder(root.left, depth+1) + [str(root.val)+'.'+str(depth)] + self.inOrder(root.right, depth+1)


# Easy Recursive Solution
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            else:
                return helper(left.left, right.right) and helper(left.right, right.left)
        return helper(root.left, root.right)


# Iterative Solution
class Solution3:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        subtree_stack = [(root.left, root.right)]

        while (len(subtree_stack)):
            left, right = subtree_stack.pop()

            if (not left and right) or (left and not right):
                return False

            if left and right:
                if left.val != right.val:
                    return False

                subtree_stack.append((left.right, right.left))
                subtree_stack.append((left.left, right.right))

        return True