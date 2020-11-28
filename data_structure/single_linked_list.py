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
        return f'Node({self.val})'


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        pass

    def __len__(self):
        return self.length

    def __iter__(self):
        n = self.head
        while n:
            yield str(n.val)
            n = n.next

    def __repr__(self):
        return '->'.join([i for i in self])

    def print_list(self):
        print(self)

    def check_index(self, idx):
        if not 0 <= idx <= self.length:
            raise IndexError('index out of range')

    def __setitem__(self, idx, value):
        self.check_index(idx)
        n = self.head
        for i in range(idx):
            n = n.next
        n.val = value

    def __getitem__(self, idx):
        self.check_index(idx)
        n = self.head
        for i in range(idx):
            n = n.next
        return n.val

    def insert_nth(self, idx, value):
        self.check_index(idx)
        n = Node(value)
        if idx == 0:
            if not self.head:
                self.head = n
            else:
                n.next = self.head
                self.head = n
        else:
            temp = self.head
            for i in range(idx - 1):
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.length += 1

    def insert_head(self, value):
        self.insert_nth(0, value)

    def insert_tail(self, value):
        self.insert_nth(self.length, value)

    def delete_nth(self, idx):
        self.check_index(idx)
        if idx == 0:
            if not self.head:
                raise IndexError('index out od range')
            else:
                del_node = self.head
                self.head = self.head.next
                self.length -= 1
                return del_node.val
        else:
            n = self.head
            for i in range(idx - 1):
                n = n.next
            del_node = n.next
            n.next = n.next.next
            del_node.next = None
            self.length -= 1
            return del_node.val

    def reverse(self):
        if self.length <= 1:
            return
        pre = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        self.head = pre

    def is_empty(self):
        return not bool(self.length)

    def delete_head(self):
        return self.delete_nth(0)

    def delete_tail(self):
        return self.delete_nth(self.length - 1)


def test_singly_linked_list() -> None:
    """
    >>> test_singly_linked_list()
    """
    linked_list = LinkedList()
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

    assert all(linked_list[i] == i + 1 for i in range(0, 9)) is True

    for i in range(0, 9):
        linked_list[i] = -i
    assert all(linked_list[i] == -i for i in range(0, 9)) is True


def main():
    from doctest import testmod

    testmod()
    linked_list = LinkedList()
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
    print(linked_list)
    linked_list.reverse()
    linked_list.print_list()

    linked_list = LinkedList()
    linked_list.insert_head(input("Inserting 1st at head ").strip())
    linked_list.insert_head(input("Inserting 2nd at head ").strip())
    print("\nPrint list:")
    linked_list.print_list()
    linked_list.insert_tail(input("\nInserting 1st at tail ").strip())
    linked_list.insert_tail(input("Inserting 2nd at tail ").strip())
    print("\nPrint list:")
    linked_list.print_list()
    print("\nDelete head")
    linked_list.delete_head()
    print("Delete tail")
    linked_list.delete_tail()
    print("\nPrint list:")
    linked_list.print_list()
    print("\nReverse linked list")
    linked_list.reverse()
    print("\nPrint list:")
    linked_list.print_list()
    print("\nString representation of linked list:")
    print(linked_list)
    print("\nReading/changing Node data using indexing:")
    print(f"Element at Position 1: {linked_list[1]}")
    linked_list[1] = input("Enter New Value: ").strip()
    print("New list:")
    print(linked_list)
    print(f"length of linked_list is : {len(linked_list)}")


if __name__ == "__main__":
    main()
