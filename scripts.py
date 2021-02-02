# -*- coding:utf-8 -*-
# @atime    : 2021/2/2 10:49 下午
"""
commit scripts
"""
import os
import sys


def local_file_test(solute_fn):
    def fun():
        test_fp = os.path.join(os.path.dirname(__file__), 'test_data')
        f1 = sys.stdin
        f = open(test_fp, 'r')
        sys.stdin = f
        res = solute_fn()
        f.close()
        sys.stdin = f1
        return res

    return fun
