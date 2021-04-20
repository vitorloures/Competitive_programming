# Kickstart Google 18/04: Problem 2 - Incomplete

import math
import os
import random
import re
import sys


def longest_progression(length: int, ai_list: list) -> int:
    diff_count = {}
    diff_list = []
    for i in range(1, length):
        ai_prior = ai_list[i-1]
        ai = ai_list[i]
        diff = ai - ai_prior
        diff_list.append(diff)
        count = diff_count.get(diff, 0)
        count += 1
        diff_count[diff] = count

    if len(diff_count) == 1:
        return list(diff_count.values())[0] + 1

    else:
        return change_one_pos(ai_list)


def get_most_frequent_diff(a_list):
    diff_count = {}
    diff_list = []
    for i in range(1, len(a_list)):
        ai_prior = a_list[i - 1]
        ai = a_list[i]
        diff = ai - ai_prior
        diff_list.append(diff)
        count = diff_count.get(diff, 0)
        count += 1
        diff_count[diff] = count
    return sorted(diff_count.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)[0][0]


def change_one_pos(an_list: list) -> int:
    big_seq = 1
    can_move = True
    if len(an_list) == 1:
        return 1

    if len(an_list) == 2:
        return 2

    original_seq = an_list.copy()
    # diff = an_list[1] - an_list[0]
    diff = get_most_frequent_diff(an_list)

    for i in range(1, len(an_list)):
        cur_diff = an_list[i] - an_list[i-1]
        if diff == cur_diff:
            big_seq += 1
        elif diff != cur_diff and can_move:
            can_move = False
            pos = i
            an_list[i] = an_list[i-1] + diff
            big_seq += 1
        elif diff != cur_diff and not can_move:
            if i != len(an_list) - 1:
                return max(big_seq, change_one_pos(original_seq[pos:]))
            else:
                return big_seq

    return big_seq


if __name__ == '__main__':
    t = int(input().split()[0])
    for i in range(t):
        case_number = i + 1
        n = int(input().split()[0])
        a_list = list(map(int, input().rstrip().split()))
        result = longest_progression(n, a_list)
        print(f"Case #{case_number}: {result}")
