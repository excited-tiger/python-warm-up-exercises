# -*- coding:utf-8 -*-
# @atime    : 2020/11/26 10:01 下午

"""
single linked list
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        print(f'Node({self.val})')


class SingleLinkedList:
    def __init__(self, val):
        self.head = Node(val)
        self.length = 1 if val is not None else 0

    def __repr__(self):
        n = self.head
        res = []
        while n:
            res.append(n)
            n = n.next
        print('-->'.join(res))

    def __setitem__(self, idx, value):
        assert idx >= 0, 'error: index less than 0'
        assert idx <= self.length, 'error: index out of range'
        n = self.head
        for i in range(idx+1):
            n = n.next
        n.val = value

    def __getitem__(self, idx):
        assert idx >= 0, 'error: index less than 0'
        assert idx <= self.length, 'error: index out of range'
        n = self.head
        for i in range(idx+1):
            n = n.next
        return n.val

    def insert_tail(self, val):
        n = self.head
        while n.next:
            n = n.next
        n.next = Node(val)

    def insert_head(self, val):
        n = Node(val)
        n.next = self.head
        self.head = n

    def insert(self, idx, val):
        assert idx >= 0, 'error: index less than 0'
        assert idx <= self.length, 'error: index out of range'
        n = self.head
        for i in range(idx -1 ):
            n = n.next
        temp_node = Node(val)
        temp_node.next = n.next
        n.next = temp_node


if __name__ == '__main__':
    pass
