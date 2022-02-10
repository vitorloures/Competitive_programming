# # Leetcode:  Pascal's Triangle (Easy)

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution = []
        last_layer = [1]
        solution.append(last_layer)
        for i in range(2, numRows+1):
            layer = [1]
            for i in range(1, len(last_layer)):
                num = last_layer[i-1] + last_layer[i]
                layer.append(num)
            layer.append(1)
            solution.append(layer)
            last_layer = layer
        return solution

sol = Solution()
print(sol.generate(5))