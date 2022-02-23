# Leetcode:  Longest Common Substring (Easy)
# Brute Force: Time: O(nlogn) Space O(N)
# DP solution: Time O(N) Space O(N)

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize for 0, 1 and 2 (first 2 power of 2)
        if n == 0:
            return [0]
        n_ones = [0, 1]
        floor_power_two = 1
        for i in range(2, n+1):
            if i == floor_power_two * 2:
                ones_i = 1
                floor_power_two *= 2
            else:
                ones_i = n_ones[i - floor_power_two] + 1
            n_ones.append(ones_i)
        return n_ones


sol = Solution()
print(sol.countBits(10))
print(sol.countBits(0))
print(sol.countBits(1))

