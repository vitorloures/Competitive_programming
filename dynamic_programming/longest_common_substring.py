# Leetcode:  Longest Common Substring (Medium)

from typing import List, Optional


class Solution:
    table: List[List[bool]]
    i_lcs: int
    j_lcs: int

    def longestPalindrome(self, s: str) -> str:
        self.build_dp_table(s)
        return s[self.i_lcs: self.j_lcs+1]

    def build_dp_table(self, s: str) -> None:
        self.i_lcs = 0
        self.j_lcs = 0
        self.table = [[False] * len(s) for i in range(len(s))]

        # Initialize one and two letters strings
        for i in range(len(s) - 1):
            self.table[i][i] = True
            if s[i] == s[i+1]:
                self.table[i][i + 1] = True
                self.track_lcs(i, i+1)

        for palindrome_length in range(3, len(s) + 1):
            i = 0
            j = palindrome_length - 1
            while j < len(s):
                if self.table[i + 1][j - 1] and s[i] == s[j]:
                    self.table[i][j] = True
                    self.track_lcs(i, j)
                i += 1
                j += 1

    def max_lcs_length(self) -> int:
        return self.j_lcs - self.i_lcs + 1

    def track_lcs(self, i: int, j: int) -> None:
        self.i_lcs = i
        self.j_lcs = j

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
print(sol.longestPalindrome("caba"))
print(sol.longestPalindrome("aaaaa"))
# print(sol.partition('aab'))