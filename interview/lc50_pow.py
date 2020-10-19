# -*- coding:utf-8 -*-
# @atime    : 2020/10/8 11:37 上午
"""
Leetcode 50 pow(m,i)
"""


def my_pow(m: int, n: int) -> float:
    """Binary Exponentiation

    Args:
        m:int,
        n:float

    Returns:pww

    """
    res = 1.0

    i = abs(n)
    while i:
        if i & 1:
            res *= m
        m *= m
        i = i >> 1
    if n < 0:
        return 1.0 / res
    return int(res)


if __name__ == '__main__':
    x = 3
    y = -13
    r = my_pow(x, y)
    print(r)
    print(x**y)