# Leetcode:  Longest Common Substring

from typing import List, Optional


class Solution:
    table: List[List[Optional[bool]]]
    i_lcs: int
    j_lcs: int

    def longestPalindrome(self, s: str) -> str:
        self.build_dp_table(s)

        for candidate_palidrome_size in range(len(s), -1, -1):
            for start_i in range(0, len(s) - candidate_palidrome_size + 1):
                candidate = s[start_i: start_i+candidate_palidrome_size]
                if self.is_palindrome(candidate, start_i,
                                      start_i+candidate_palidrome_size-1):
                    return candidate

    def build_dp_table(self, s: str) -> None:
        for i in range(len(s)):
            for j in range(i, len(s)):
                if i == j:
                    self.table[i][i] = True
                elif j == i + 1:
                    self.table[i][j] = s[i] == s[j]
                else:
                    self.table[i][j] = self.table[i+1][j-1] and s[i] == s[j]

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        if self.table[start][end]:
            return self.table[start][end]
        if len(s) == 1 or len(s) == 0:
            self.table[start][end] = True
            return True
        if s[0] != s[-1]:
            self.table[start][end] = False
            return False
        return self.is_palindrome(s[1:-1], start, end)


sol = Solution()
print(sol.longestPalindrome("babad"))
# print(sol.partition('aab'))