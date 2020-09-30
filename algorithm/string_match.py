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
                break
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


def bm(text, pattern):
    """BM algorithm

    Args:
        text (str):
        pattern (str):

    Returns: (int) if not match: -1

    """
    # get char idx from right in pattern
    pat_char_right_idx_dict = {}
    for idx, char in enumerate(pattern):
        pat_char_right_idx_dict[char] = len(pattern) - idx

    # get longest public str from front and end
    good_str_idx_dict = {}
    for st in range(0, len(pattern)):
        for end in range(st + 1, len(pattern) + 1):
            good_str = pattern[st:end]
            if good_str not in good_str_idx_dict:
                good_str_idx_dict[good_str] = st

    cur_idx, match_char_idx = len(pattern) - 1, len(pattern) - 1
    match_char_num, move_idx = 0, 0
    while 0 <= cur_idx < len(text):

        if text[cur_idx] == pattern[match_char_idx]:
            match_char_num += 1
            match_char_idx -= 1
            if match_char_num == len(pattern):
                return cur_idx
        else:
            # bad char
            if text[cur_idx] in pat_char_right_idx_dict:
                bad_move_idx = pat_char_right_idx_dict[text[cur_idx]] - (
                    len(pattern) - match_char_idx)
            else:
                bad_move_idx = len(pattern)
            match_char_idx = len(pattern) - 1
            if text[cur_idx] in pattern:
                if match_char_num:
                    max_len_str = pattern[-match_char_num:]
                    for i in range(len(max_len_str)):
                        i += 1
                        pat_idx = len(pattern) - i
                        k = max_len_str[-i:]
                        gd_idx = good_str_idx_dict.get(k, -1)

                        move_idx = pat_idx - gd_idx
            move_idx = max(move_idx, bad_move_idx)
            cur_idx += move_idx
            match_char_num = 0
            move_idx = 0
            continue

        cur_idx -= 1
    return -1


if __name__ == '__main__':
    t = 'to young too simple'
    p = 'too'
    # res = sunday(t, p)
    res = bm(t, p)
    print(res)
    pass
