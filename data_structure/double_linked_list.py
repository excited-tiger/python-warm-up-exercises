# -*- coding:utf-8 -*-
# @atime    : 2020/11/28 10:07 下午

"""
double linked list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.pre = None
        self.next = None

    def __str__(self):
        return f'{self.data}'


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        n = self.head
        while n:
            yield str(n.data)
            n = n.next

    def __len__(self):
        return self.length

    def __str__(self):
        return '->'.join(self)

    def delete(self, data):
        n = self.head
        while n:
            if n.data == data:
                break
            n = n.next
        if not n or n.data != data:
            raise IndexError
        self.length -= 1
        if not n.pre:
            return self.delete_head()
        elif not n.next:
            return self.delete_tail()
        else:
            pre = n.pre
            pre.next = n.next
            n.next.pre = pre
            return n

    def delete_nth(self, index):
        if not 0 <= index < self.length:
            raise IndexError
        if index == 0:
            if not self.head:
                raise IndexError
            del_node = self.head
            self.head = self.head.next
            self.head.pre = None
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            del_node = cur
            if index == self.length - 1:
                self.tail = cur.pre
                cur.pre.next = None
            else:
                pre = cur.pre
                pre.next = cur.next
                cur.next.pre = pre

        del_node.next = None
        del_node.pre = None
        self.length -= 1
        return del_node.data

    def delete_head(self):
        return self.delete_nth(0)

    def delete_tail(self):
        return self.delete_nth(self.length - 1)

    def insert_nth(self, index, data):
        if not 0 <= index <= self.length:
            raise IndexError
        if index == 0:
            n = Node(data)
            if not self.head:
                self.head = n  # raise IndexError
            else:
                n.next = self.head
                self.head.pre = n
                self.head = n
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            n = Node(data)
            if not cur.next:
                self.tail = n
            n.next = cur.next
            n.pre = cur
            cur.next = n
        self.length += 1

    def insert_head(self, data):
        self.insert_nth(0, data)

    def insert_tail(self, data):
        self.insert_nth(self.length, data)

    def is_empty(self):
        return not bool(self.length)


def test_doubly_linked_list() -> None:
    """
    >>> test_doubly_linked_list()
    """
    linked_list = DoubleLinkedList()
    assert linked_list.is_empty() is True
    assert str(linked_list) == ""

    try:
        linked_list.delete_head()
        assert False  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    try:
        linked_list.delete_tail()
        assert False  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    for i in range(10):
        assert len(linked_list) == i
        linked_list.insert_nth(i, i + 1)
    assert str(linked_list) == "->".join(str(i) for i in range(1, 11))

    linked_list.insert_head(0)
    linked_list.insert_tail(11)
    assert str(linked_list) == "->".join(str(i) for i in range(0, 12))
    assert linked_list.delete_head() == 0

    assert linked_list.delete_nth(9) == 10

    assert linked_list.delete_tail() == 11
    assert len(linked_list) == 9
    assert str(linked_list) == "->".join(str(i) for i in range(1, 10))


if __name__ == "__main__":
    # from doctest import testmod
    # testmod()
    test_doubly_linked_list()
