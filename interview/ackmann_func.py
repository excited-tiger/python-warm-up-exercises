# -*- coding:utf-8 -*-
# @atime    : 2020/12/2 8:36 下午

"""
Ackmann func
http://wikioi.cn/problem/23082
"""


def akm(m: int, n: int) -> int:
    """
    Ackmann 函数
    Args:
        m (int):m >= 0
        n (int):n >= 0
    Returns: int
    """
    assert m >= 0 and n >= 0, 'm, n must greater than 0'
    if m == 0:
        return n + 1
    elif n == 0:
        return akm(m - 1, 1)
    else:
        # n > 0
        return akm(m - 1, akm(m, n - 1))


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    res = akm(x, y)
    print(res)

