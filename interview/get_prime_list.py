# -*- coding:utf-8 -*-
"""
get a list of prime numbers less than n
"""


def get_prime_list_v1(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    prime_num_list = [2]

    def add_prime_num(n, prime_list):
        # 进1取整
        # m = int(round(math.sqrt(n), 0))
        if n < 3:
            return prime_list
        flag = True
        for prime in prime_list:
            # global count
            if prime**2 > n:
                break
            if n % prime == 0:
                flag = False
                break
        if flag:
            prime_list.append(n)
        return prime_list

    for i in range(2, n + 1):
        prime_num_list = add_prime_num(i, prime_num_list)
    # print(count)
    return prime_num_list


def get_prime_list(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    prime_list = [2]
    count = 0
    for i in range(3, n + 1):
        for j in prime_list:
            count += 1
            if i % j == 0:
                break
            elif j * j > i:
                prime_list.append(i)
                break
    # print(count)
    return prime_list


if __name__ == '__main__':
    # res = get_prime_list_v1(3000)
    res = get_prime_list(3000)
    print(res)