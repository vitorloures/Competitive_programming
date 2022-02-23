# # Leetcode:  Maximum Subarray (Easy)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if num > cur_sum:
                cur_sum = num

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum


sol = Solution()
# print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4,10]) == 15
assert sol.maxSubArray([1]) == 1
assert sol.maxSubArray([5,4,-1,7,8]) == 23
