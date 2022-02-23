# Leetcode: Intersection of Two Sum (Easy)

from typing import  List


# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] = i

        for i in range(len(nums)):
            complementary = target - nums[i]
            if hash_table.get(complementary) and hash_table.get(complementary) != i:
                return [i, hash_table[complementary]]


sol = Solution()
assert sol.twoSum([2, 7, 11, 15], target=9) == [0, 1]
assert sol.twoSum([3,2,4], target=6) == [1, 2]
assert sol.twoSum([3,3], target=6) == [0, 1]
assert sol.twoSum([1,3,4,2], target=6) == [2, 3]
