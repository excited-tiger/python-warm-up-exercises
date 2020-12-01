# -*- coding:utf-8 -*-
# @atime    : 2020/12/1 8:45 上午

"""
disjoint_set practise
https://www.luogu.com.cn/problem/P1197
"""
from typing import List


class Disjoint():
    def __init__(self, data):
        self.data = data
        self.parent = self


def find(n: Disjoint) -> Disjoint:
    while n.parent != n:
        n = n.parent
    return n


def merge(x: Disjoint, y: Disjoint) -> tuple:
    """
    合并
    Args:
        x (Disjoint):
        y (Disjoint):

    Returns:
        x (Disjoint), y (Disjoint)
    """
    x_p = find(x)
    y_p = find(y)
    if x_p == x and y_p == y:
        x.parent = y_p
    elif x_p == x and y_p != y:
        x.parent = y_p
        # 路径压缩
        y.parent = y_p
    elif x_p != x and y_p == y:
        y.parent = x_p
        # 路径压缩
        x.parent = x_p
    else:
        # x_p != x and y_p != y:
        x.parent = y.parent = y_p
    return x, y


def parse_data(input_str: str) -> tuple:
    """
    解析输入数据
    Args:
        input_str (str):输入的字符串

    Returns: tuple
        行星个数 int
        行星可以连接的所有组合 list
        要摧毁的所有行星 list
    """
    union_list = []
    destroy_list = []

    input_str_list = input_str.split('\n')
    planet_num, union_num, destroy_num = 0, 0, 0

    for line in input_str_list:
        line = line.strip()
        if not line:
            continue
        line_list = line.split(' ')
        if len(line_list) > 1:
            if not planet_num and not union_num:
                planet_num, union_num = int(line_list[0]), int(line_list[1])
            else:
                union_list.append((int(line_list[0]), int(line_list[1])))
        else:
            if not destroy_num:
                destroy_num = int(line_list[0])
            else:
                destroy_list.append(int(line_list[0]))
    return planet_num, union_list, destroy_list


def main(input_str: str) -> str:
    """
    Args:
        input_str (str):输入的字符串数据
    Returns: output str 连通块个数
    """
    # 1. 解析数据
    planet_num, union_list, destroy_list = parse_data(input_str)

    # 2. 连通块个数
    members = list(range(planet_num))
    # 初始状态连通块个数
    origin_set_num, union_list = get_union_num(union_list, members=members)
    final_res = [str(origin_set_num)]
    # 获取每次打击后的连通块个数
    for idx, i in enumerate(destroy_list):
        members.remove(i)
        union_num, union_list = get_union_num(union_list, members=members,
                                              destroy=i)
        final_res.append(str(union_num))

    return '\n'.join(final_res)


def get_union_num(union_list: List[tuple], members: list,
                  destroy=None) -> tuple:
    """
    根据集合组合 计算 最终的联通的区域个数
    Args:
        union_list (List(tuple)): 行星组合
        members (list):所有行星
        destroy (int):要摧毁的行星
    Returns:
        联通区域的个数, 摧毁掉行星后，行星的组合
    """
    parent_list = []
    new_union_list = []
    members_map = {i: Disjoint(i) for i in members}
    for x, y in union_list:
        if destroy is not None and destroy in [x, y]:
            continue
        new_union_list.append((x, y))
        members_map[x], members_map[y] = merge(members_map[x], members_map[y])
    for p in members_map:
        m = members_map[p]
        m = find(m)
        if m not in parent_list:
            parent_list.append(m)
    return len(parent_list), new_union_list


def main2(input_str):
    # 1. 解析数据
    planet_num, union_list, destroy_list = parse_data(input_str)
    final_res = []
    total_members_map = {i: Disjoint(i) for i in range(planet_num)}

    iter_nums = len(destroy_list) + 1
    for _ in range(iter_nums):
        next_iter_union_list = []
        temp_union_list = []
        for x, y in union_list:
            if x in destroy_list or y in destroy_list:
                next_iter_union_list.append((x, y))
                continue
            total_members_map[x], total_members_map[y] = merge(
                total_members_map[x], total_members_map[y])

        for i in total_members_map:
            if i not in destroy_list:
                i_p = find(total_members_map[i])
                if i_p.data not in temp_union_list:
                    temp_union_list.append(i_p.data)

        final_res.append(str(len(temp_union_list)))
        union_list = next_iter_union_list

        if destroy_list:
            destroy_list.pop()
    return '\n'.join(final_res[::-1])


if __name__ == '__main__':
    input_ = """
    8 13
0 1
1 6
6 5
5 0
0 6
1 2
2 3
3 4
4 5
7 1
7 2
7 6
3 6
5
1
6
3
5
7
    """
    """
    解法一：正常思维 
        1. 先计算没有被攻击时所有的连通块个数
        2. 记录每次攻击后新的组合和没有被攻击的行星
        3. 遍历没有被攻击的行星，找其根节点，计算根节点的数目就是连通块个数
        4. 再遍历新的组合 计算连通块个数（会重复遍历）
    """
    # main(input_)
    """
    解法二：逆向思维
        1. 被摧毁最多-> 没有被摧毁，由最少组合不断扩充，减少遍历次数
    """
    main2(input_)
