# -*- coding:utf-8 -*-
# @atime    : 2020/12/2 9:15 下午
"""
P2024 [NOI2001]食物链
https://www.luogu.com.cn/problem/P2024
解析：https://web.archive.org/web/20181221195539/https://agatelee.cn/2017/05/
%e5%b8%a6%e6%9d%83%e5%b9%b6%e6%9f%a5%e9%9b%86/
"""
parents = [i for i in range(50001)]
weights = [0 for _ in range(50001)]  # 0：同类 1：吃 2：被吃
false_count = 0


def parse_data(input_str: str) -> tuple:
    """
    解析输入的数据
    Args:
        input_str (str):输入的数据
    Returns:
        N, K, sentences
    """
    line_list = input_str.strip().split('\n')
    sentences = []
    n, k = 0, 0
    for line in line_list:
        line = line.strip()
        if not line:
            continue
        temp_ls = line.split(' ')
        if len(temp_ls) == 2:
            n, k = int(temp_ls[0]), int(temp_ls[1])
        else:
            sentences.append([int(i) for i in temp_ls])
    return n, k, sentences


def find(x):
    # x 1 3 8
    #   3 8 8
    if x != parents[x]:
        temp = parents[x]
        parents[x] = find(parents[x])
        weights[x] = (weights[x] + weights[temp]) % 3
    return parents[x]


def merge(x, y, relation):
    x_p = find(x)
    y_p = find(y)
    global false_count
    if x_p == y_p:
        if (relation - 1) != ((weights[x] - weights[y] + 3) % 3):
            false_count += 1
    else:
        parents[x_p] = y_p
        weights[x_p] = (weights[y] - weights[x] + relation - 1) % 3


def solution(input_str: str):
    """
    解法
    Args:
        input_str (str):输入的数据
    Returns:
        out_str
    """
    global false_count
    n, k, sentences = parse_data(input_str)
    # N（1 <= N <= 50,000）和K句话（0 <= K <= 100,000），
    for r, x, y in sentences:
        if x > n or y > n or (r == 2 and x == y):
            false_count += 1
        else:
            merge(x, y, r)
    print(false_count)


def main():
    input_s = input('n, k')
    n, k = input_s.strip().split()
    n, k = int(n), int(k)
    for i in range(k):
        input_s += '\n' + input()
    solution(input_s)


if __name__ == '__main__':
    s = """
100 7
1 101 1 
2 1 2
2 2 3 
2 3 3 
1 1 3 
2 3 1 
1 5 5    
"""

    f = "/Users/sunzhenping/Downloads/P2024_2.in"
    with open(f, 'r', encoding='u8') as f1:
        s = f1.read()
    solution(s)
