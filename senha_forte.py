#!/bin/python3

import math
import os
import random
import re
import sys


def has_number(string_test):
    return bool(re.search(r'\d', string_test))


def has_lower(string_test):
    return bool(re.search('[a-z]', string_test))


def has_upper(string_test):
    return bool(re.search('[A-Z]', string_test))


def has_special(string_test):
    return bool(re.search('[@_!#$%^&*()<>?/\|}{~:]', string_test))
    # regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')


def check_password(length, string_test):
    number = has_number(string_test)
    upper = has_upper(string_test)
    lower = has_lower(string_test)
    special = has_special(string_test)
    all = number + upper + lower + special
    miss_pattern = 4 - all
    miss_length = len(string_test) - length
    miss = max(miss_length, miss_pattern)
    return miss


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().split()[0])
    string = str(input().split()[0])
    # ar = list(map(int, input().rstrip().split()))

    result = check_password(n, string)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()