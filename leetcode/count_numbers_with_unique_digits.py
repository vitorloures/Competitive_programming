# Leetcode: Count Numbers with Unique Digits (Medium)

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        total_unique = 1
        n_dig_unique = 1
        pos_for_n = 9
        for i in range(1, n + 1):
            n_dig_unique *= pos_for_n
            total_unique += n_dig_unique
            pos_for_n -= 1

            if i == 1:
                pos_for_n = 9

        return total_unique

sol = Solution()
assert sol.countNumbersWithUniqueDigits(0) == 1
assert sol.countNumbersWithUniqueDigits(2) == 91
