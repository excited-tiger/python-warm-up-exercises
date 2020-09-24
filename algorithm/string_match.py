# -*- coding:utf-8 -*-
# @atime    : 2020/9/19 11:01 下午


def sunday(text, pattern):
    """sunday string match

    Args:
        text, pattern

    Returns:
        int: match index, -1: not match
    """
    # get index from right
    char_right_idx_dict = dict()
    for i in range(len(pattern)):
        # right pos char will replace left
        char_right_idx_dict[pattern[i]] = len(pattern) - i
    cur_idx = 0
    match_char_num = 0
    while cur_idx < len(text):
        if text[cur_idx] == pattern[match_char_num]:
            match_char_num += 1
            if match_char_num == len(pattern):
                return cur_idx + 1 - len(pattern)
        else:
            next_char_idx = cur_idx - match_char_num + len(pattern)
            if next_char_idx < len(text):
                move_idx = char_right_idx_dict.get(text[next_char_idx],
                                                   len(pattern) + 1)
                cur_idx += move_idx - match_char_num
                match_char_num = 0
                continue
        cur_idx += 1
    return -1


def kmp(text, pattern):
    """KMP algorithm

    Args:
        text (str):
        pattern (str):

    Returns:
        idx (int): -1: not match
    """
    longest_pub_str_list = [0] * len(pattern)
    for patt_len in range(len(pattern), 0, -1):
        temp_pattern = pattern[:patt_len]
        longest_len = 0
        for pub_str_len in range(len(temp_pattern), 0, -1):
            # not include self
            pub_str_len -= 1
            front_pub_str = temp_pattern[:pub_str_len]
            end_pub_str = temp_pattern[-pub_str_len:]
            if front_pub_str == end_pub_str:
                longest_len = pub_str_len
        longest_pub_str_list[patt_len - 1] = longest_len
    cur_idx = 0
    match_char_num = 0
    while cur_idx < len(text) and match_char_num < len(pattern):
        if text[cur_idx] == pattern[match_char_num]:
            match_char_num += 1
            if match_char_num == len(pattern):
                return cur_idx + 1 - match_char_num
        else:
            if match_char_num:
                cur_idx += match_char_num - longest_pub_str_list[match_char_num
                                                                 - 1]
                match_char_num = 0
                continue
        cur_idx += 1

    return -1


if __name__ == '__main__':
    t = 'BBC ABCDAB ABCDABCDABDE'
    p = 'ABCDABD'
    # res = sunday(t, p)
    res = kmp(t, p)
    print(res)
    pass
