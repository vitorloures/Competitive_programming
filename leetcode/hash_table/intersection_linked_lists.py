# Leetcode: Intersection of Two Linked Lists (Easy)

from typing import  Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Time: O(N+M)
# Space: O(N)
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_a = {}
        node = headA
        count = 1
        while node is not None:
            nodes_a[node] = count
            count += 1
            node = node.next

        node = headB
        while node is not None:
            if nodes_a.get(node):
                return node
            node = node.next

        return None


# Time: O(N+M)
# Space: O(1)
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        if not p1 or not p2:
            return None

        while p1 and p2:
            if p1 == p2:
                return p1

            if p1.next:
                p1 = p1.next
            else:
                p1 = headB

            if p2.next:
                p2 = p2.next

            else:
                p2 = headA

        return None

