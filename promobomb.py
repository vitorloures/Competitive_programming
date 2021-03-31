#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict


def calc_profit(n_people):
    r = 4 * n_people ** 2
    c = 100 * n_people
    return r - c


if __name__ == '__main__':
    n = int(input().split()[0])

    profit_dict = OrderedDict()

    for i in range(n):
        line = input().split('\'')
        name = line[1]
        x = int(line[2])
        profit = calc_profit(x)
        profit_dict[i+1] = profit

    profit_descending = sorted(profit_dict.items(),
                               key=lambda kv: kv[1], reverse=True)
    # print(profit_descending)
    first = profit_descending[0][0]
    print(first)
    second = profit_descending[1][0]
    print(second)
    third = profit_descending[2][0]
    print(third)
