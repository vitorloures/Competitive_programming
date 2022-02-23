# Leetcode: Find Center of Star Graph (Easy)

from typing import List


"""
mat -> FlatMap -> new_mat 

In FlatMap 

mat[i][j] -> FlatMap[i * m + j] = [ip * c + jp] -> newmat[ip][jp]

ip = (i * m + j) // c

"""


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if n * m != r * c:
            return mat

        new_mat = [[None for j in range(c)] for i in range(r)]
        for i in range(m):
            for j in range(n):
                ip = (i * n + j) // c
                jp = (i * n + j) % c
                new_mat[ip][jp] = mat[i][j]

        return new_mat


sol = Solution()
assert sol.matrixReshape([[1,2,3,4],[5,6,7,8]], 4, 2) == [[1,2],[3,4],[5,6],[7,8]]

