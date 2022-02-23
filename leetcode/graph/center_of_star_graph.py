# Leetcode: Find Center of Star Graph (Easy)

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        steps = 2
        edge_counter = {}
        for i in range(steps):
            edge = edges[i]
            first_node, second_node = edge
            if edge_counter.get(first_node):
                edge_counter[first_node] += 1
            else:
                edge_counter[first_node] = 1

            if edge_counter.get(second_node):
                edge_counter[second_node] += 1
            else:
                edge_counter[second_node] = 1

        for node_value, freq in edge_counter.items():
            if freq == 2:
                return node_value
        raise Exception("Solution Error")


sol = Solution()
assert sol.findCenter([[1,2],[2,3],[4,2]]) == 2
assert sol.findCenter([[1,2],[5,1],[1,3],[1,4]]) == 1