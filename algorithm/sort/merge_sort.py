# -*- coding:utf-8 -*-
# @atime    : 2021/2/22 22:59
"""
merge sort
"""


def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    half = len(num_list) // 2
    left_list = merge_sort(num_list[:half])
    right_list = merge_sort(num_list[half:])
    min_len = min(len(left_list), len(right_list))
    sort_list = []
    i, j = 0, 0
    while i < min_len and j < min_len:
        if left_list[i] < right_list[j]:
            sort_list.append(left_list[i])
            i += 1
        else:
            sort_list.append(right_list[j])
            j += 1
    while i < len(left_list):
        sort_list.append(left_list[i])
    while j < len(right_list):
        sort_list.append(right_list[j])
    return sort_list


if __name__ == '__main__':
    n = [13, 12, 5, 8, 3, 21, 14, 9]
    res = merge_sort(n)
    print(res)
