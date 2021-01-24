# -*- coding:utf-8 -*-
# @atime    : 2021/1/24 12:58 下午
"""
edit distance
https://leetcode-cn.com/problems/edit-distance/
"""


def solution1(word1: str, word2: str):
    """
    计算编辑距离
    Args:
        word1 (str): 字符串1
        word2 (str): 字符串2

    Returns: (int) distance
    """
    if not word1 or not word2:
        return max(len(word1), len(word2))
    if word1 == word2:
        return 0
    res = []
    for i in range(len(word1) + 1):
        line_res = []
        for j in range(len(word2) + 1):
            if i == 0:
                line_res.append(j)
                continue
            if j == 0:
                line_res.append(i)
            else:
                if word1[i - 1] == word2[j - 1]:
                    line_res.append(res[i - 1][j - 1])
                else:
                    temp_dis = min(res[i - 1][j - 1], res[i - 1][j], line_res[j - 1]) + 1
                    line_res.append(temp_dis)
        res.append(line_res)
    return res[-1][-1]


def solution2(word1, word2):
    l1, l2 = len(word1), len(word2)
    if not word1 or not word2:
        return max(l1, l2)
    if word1 == word2:
        return 0
    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
    for i in range(l1 + 1):
        for j in range(l2 + 1):
            if i == 0:
                dp[i][j] = j
                continue
            if j == 0:
                dp[i][j] = i
            else:
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[-1][-1]


def solution3(word1, word2):
    from heapq import heappop, heappush
    heap = [(0, word1, word2)]
    visited_set = set()
    while heap:
        d, w1, w2 = heappop(heap)
        if (w1, w2) in visited_set:
            continue
        visited_set.add((w1, w2))
        if w1 == w2:
            return d
        if w1 and w2 and w1[0] == w2[0]:
            heappush(heap, (d, w1[1:], w2[1:]))
        else:
            if w1:
                heappush(heap, (d + 1, w1[1:], w2))  # delete
            if w2:
                heappush(heap, (d + 1, w1, w2[1:]))  # add
            if w1 and w2:
                heappush(heap, (d + 1, w1[1:], w2[1:]))  # replace


if __name__ == '__main__':
    r = solution3('abc', 'agcag')
    print(r)
    pass
