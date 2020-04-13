# coding=utf-8

import numpy as np


def xuanze_sort(lst):
    if len(lst) <= 0:
        return -1
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


nums = np.random.randint(200, size=10)
print(nums)
print(xuanze_sort(nums))
# 0   1       173 191 42 51
# 0   2       173 191 42 51
# 0   3       42 191 173 51
# 1   2       42 173 191 51
# 1   3       42 51 191 173
