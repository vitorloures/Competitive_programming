# Leetcode: Valid Sudoku Solution (Medium)


from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_val_rules = [{} for i in range(9)]
        cols_val_rules = [{} for i in range(9)]
        boxes_val_rules = [{} for i in range(9)]

        if len(board) != 9 or len(board[0]) != 9:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                dig = board[i][j]
                if dig != ".":
                    if not self.is_valid(dig, rows_val_rules[i], cols_val_rules[j],
                                    boxes_val_rules[self.get_boxes_index(i, j)]):
                        return False
                    rows_val_rules[i][dig] = 1
                    cols_val_rules[j][dig] = 1
                    boxes_val_rules[self.get_boxes_index(i, j)][dig] = 1

        return True

    def get_boxes_index(self, i, j):
        i = int(i)
        j = int(j)

        return i // 3 * 3 + j // 3

    def is_valid(self, dig, row, col, box):
        if row.get(dig):
            return False

        if col.get(dig):
            return False

        if box.get(dig):
            return False

        return True


sol = Solution()
assert sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]) == True

assert sol.isValidSudoku([[".","4","6",".",".",".","6",".","."],
                          [".",".",".","6",".",".",".",".","4"],
                          [".",".",".",".",".","1",".",".","."],
                          [".",".",".",".",".","7",".",".","."],
                          ["5",".","7",".",".",".","4",".","."],
                          [".",".",".",".",".",".",".",".","3"],
                          [".",".",".","7",".",".","1",".","."],
                          [".",".",".",".",".",".",".",".","."],
                          [".",".","1","2",".",".",".",".","."]]) == False