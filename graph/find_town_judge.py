# Leetcode: Find the Town Judge (Easy)

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        candidates = list(range(1, n+1))
        frequency_trusted = {}
        for pair in trust:
            trusting, trusted = pair
            if trusting in candidates:
                candidates.remove(trusting)
            if frequency_trusted.get(trusted):
                frequency_trusted[trusted] += 1
            else:
                frequency_trusted[trusted] = 1
        if len(candidates) == 0:
            return -1
        for candidate in candidates:
            if frequency_trusted.get(candidate) == n-1:
                return candidate

        return -1


sol = Solution()
assert sol.findJudge(n = 2, trust = [[1,2]]) == 2
assert sol.findJudge(n = 3, trust = [[1,3],[2,3]]) == 3
assert sol.findJudge(n = 3, trust = [[1,3],[2,3],[3,1]]) == -1

