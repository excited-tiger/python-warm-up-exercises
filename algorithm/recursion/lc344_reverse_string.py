# -*- coding:utf-8 -*-
# @atime    : 2020/11/8 9:17 下午
"""
reverse string
"""
from typing import List


class Solution:
    def reverse_string(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

    def reverse_string_recursion(self, s: List[str]):
        if len(s) <= 1:
            return s

        left_s = s[:len(s) // 2]
        right_s = s[len(s) // 2:]
        return self.reverse_string_recursion(right_s) + self.reverse_string_recursion(left_s)


if __name__ == '__main__':
    so = Solution()
    test_string = ['h', 'e', 'l', 'l', 'o']
    res = so.reverse_string_recursion(test_string)
    print(res)
