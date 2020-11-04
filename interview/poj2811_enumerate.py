# -*- coding:utf-8 -*-
# @atime    : 2020/11/3 3:06 下午
"""
poj 2811 熄灯问题 枚举（enumerate）
"""
import sys
from copy import deepcopy


def main():
    light_matrix = []
    for i in range(5):
        input_str = input('请输入灯的状态\n')
        light_matrix.append([i for i in input_str.strip().split(' ') if i])

    # 第一行开关确定下以后，后面的结果就确定了
    # 第一行开关的组合有2^6种
    total_combination_ls = []
    for i in range(2**(len(light_matrix[0]))):
        # 对应的组合 刚好是二进制数
        # {:0{}b} {:08b} 二进制数 用0填充8位
        str_i = '{:0{}b}'.format(i, len(light_matrix[0]))

        total_combination_ls.append(str_i)

        press_matrix = [['0' for i in range(len(light_matrix[0]))]
                        for j in range(len(light_matrix))]
        temp_light_matrix = deepcopy(light_matrix)
        # 改变第一行灯的状态
        for x_id, x in enumerate(str_i):
            if x == '1':
                press_matrix[0][x_id] = '1'
                temp_light_matrix = close_light(temp_light_matrix, [0, x_id])
        # 判断是否所有的灯都熄灭了 并返回按压过的结果
        bool_res, press_matrix = is_closed_all(temp_light_matrix, press_matrix)

        if bool_res:
            press_str = '\n'.join([' '.join(i) for i in press_matrix])
            # print(press_str)
            sys.stdout.write(press_str)
            return press_str


def is_closed_all(light_matrix: list, press_matrix: list) -> tuple:
    y = 0
    while y < len(light_matrix) - 1:
        y += 1
        for x_id, x in enumerate(light_matrix[y - 1]):
            if x == '1':
                press_matrix[y][x_id] = '1'
                light_matrix = close_light(light_matrix, [y, x_id])
    for light in light_matrix[y]:
        if light == '1':
            return False, []
    return True, press_matrix


def close_light(light_matrix: list, light_pos: list) -> list:
    min_x, max_x, min_y, max_y = 0, len(
        light_matrix[0]) - 1, 0, len(light_matrix) - 1
    y, x = light_pos
    # 上下左右
    target_pos = [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1], [y, x]]
    for temp_y, temp_x in target_pos:
        if temp_x < min_x or temp_x > max_x or temp_y < min_y or temp_y > max_y:
            continue
        light_matrix[temp_y][
            temp_x] = '1' if light_matrix[temp_y][temp_x] == '0' else '0'
    return light_matrix


if __name__ == '__main__':
    t = """
0 1 1 0 1 0
1 0 0 1 1 1
0 0 1 0 0 1
1 0 0 1 0 1
0 1 1 1 0 0"""

    main()
