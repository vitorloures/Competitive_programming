# Kickstart Google 18/04: Problem 1 - Total score 12/12

import math
import os
import random
import re
import sys


def get_increasing_substring(strlen: int, string: str) -> str:
    last_letter_number = ord(string[0])
    inc_str = '1 '
    last_inc_size = 1
    for i in range(1, strlen):
        cur_letter_number = ord(string[i])
        if cur_letter_number > last_letter_number:
            last_inc_size += 1
            inc_str += str(last_inc_size) + ' '
        else:
            inc_str += '1 '
            last_inc_size = 1

        last_letter_number = cur_letter_number
    return inc_str


if __name__ == '__main__':
    n = int(input().split()[0])

    for i in range(n):
        case_number = i + 1
        string_length = int(input().split()[0])
        string_to_analyse = str(input().split()[0]).upper().strip()
        result = get_increasing_substring(string_length, string_to_analyse)

        print(f"Case #{case_number}: {result}")
