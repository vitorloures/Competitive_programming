import math

"""
This code passes in the Sample test, but not in the first test for Hex problem

This implementation can always recognizes the winner, but it fails to identify
some impossible states. It provides a false positive for some cases when we have one 
single connected set touching many parts of both borders. 

It could be solved using the concept of connected set and implementing a data structuce for 
this.
"""


def main():
    T = int(input().split()[0])
    nobody = "Nobody wins"
    blue = "Blue wins"
    red = "Red wins"
    impossible = "Impossible"

    for test_i in range(1, T+1):
        result = ""
        n = int(input().split()[0])
        board = []
        word_counter = {"B": 0, "R": 0, ".": 0}
        r_win = 0
        b_win = 0
        for i in range(n):
            board.append(str(input().split()[0]))
            for j in range(n):
                word_counter[board[i][j]] += 1

        # Blue path
        for i in range(n):
            j = 0
            if has_winner_path(board, i, j, n, "B"):
                result = blue
                # b_win += 1

        # Red Path
        for j in range(n):
            i = 0
            if has_winner_path(board, i, j, n, "R"):
                result = red
                # r_win += 1

        n_b = word_counter["B"]
        n_r = word_counter["R"]

        multiple_r_win = (result == red) and has_multiple_wins(board, n, "R")
        multiple_b_win = (result == blue) and has_multiple_wins(board, n, "B")

        if math.fabs(n_b - n_r) > 1 or multiple_b_win or multiple_r_win:
            result = impossible

        if result == "":
            result = nobody

        print(f"Case #{test_i}: {result}")


def has_multiple_wins(board, n, color):
    start_edge = 0
    end_edge = n - 1
    freq_start = 0
    freq_end = 0
    for i in range(n):
        if color == "B" and board[i][start_edge] == "B":
            freq_start += 1
        if color == "B" and board[i][end_edge] == "B":
            freq_end += 1
        if color == "R" and board[start_edge][i] == "R":
            freq_start += 1
        if color == "R" and board[end_edge][i] == "R":
            freq_end += 1
    if freq_start > 1 and freq_end > 1:
        return True
    else:
        return False


def has_winner_path(board, i, j, n, color, come_from_back = False):
    if i < 0 or i >= n or j < 0 or j >= n:
        return False

    if board[i][j] != color:
        return False

    if color == "B" and j == n-1:
        return True

    if color == "R" and i == n-1:
        return True

    if color == "B":
        stmt1 = has_winner_path(board, i, j + 1, n, color, False) or \
               has_winner_path(board, i-1, j+1, n, color, False) or \
               has_winner_path(board, i+1, j, n, color, come_from_back)
        if not come_from_back:
            stmt2 = has_winner_path(board, i -1, j, n, color, True)
        else:
            stmt2 = False
        return stmt1 or stmt2

    if color == "R":
        stmt1 = has_winner_path(board, i + 1, j, n, color, False) or \
                has_winner_path(board, i + 1, j - 1, n, color, False) or \
                has_winner_path(board, i, j + 1, n, color, come_from_back)
        if not come_from_back:
            stmt2 = has_winner_path(board, i, j - 1, n, color, True)
        else:
            stmt2 = False
        return stmt1 or stmt2


if __name__ == "__main__":
    main()
