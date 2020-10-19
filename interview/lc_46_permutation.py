# -*- coding:utf-8 -*-
# @atime    : 2020/10/17 6:14 下午
"""
permutation
"""


def my_permutation(nums: list) -> list:
    """backtrack

    Args:
        nums (list)

    Returns:
        permutation_list
    """
    res = []
    visited_list = [0] * len(nums)

    def dfs(path_list):

        if len(path_list) == len(nums):
            res.append(path_list)
        else:
            for i in range(len(nums)):
                if not visited_list[i]:
                    visited_list[i] = 1
                    dfs(path_list + [nums[i]])
                    visited_list[i] = 0

    dfs([])
    return res


if __name__ == '__main__':
    n = [1, 3, 5]
    permutation_list = my_permutation(n)
    print(permutation_list)
    pass
