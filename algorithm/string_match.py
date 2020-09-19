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
    if len(text) < len(pattern):
        return -1
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
                cur_idx += move_idx
                match_char_num = 0
                continue
            else:
                return -1
        cur_idx += 1
    return -1


if __name__ == '__main__':
    t = 'gergregeagbb'
    p = 'bb'
    res = sunday(t, p)
    print(res)
    pass
