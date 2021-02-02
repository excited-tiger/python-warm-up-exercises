# -*- coding:utf-8 -*-
# @atime    : 2021/2/2 9:09 下午
"""
brackets balance
https://www.luogu.com.cn/problem/UVA673
"""


def check_balance(brackets_str):
    balance_dict = {']': '[', ')': '('}
    check_stack = []
    for i in brackets_str:
        if i in balance_dict:
            if not check_stack:
                return False
            if check_stack.pop() != balance_dict[i]:
                return False
        else:
            check_stack.append(i)
    if check_stack:
        return False
    return True


# @local_file_test
def solution():
    pair_num = int(input())
    for i in range(pair_num):
        if check_balance(input()):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    solution()
    pass
