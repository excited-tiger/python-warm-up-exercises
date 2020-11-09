# -*- coding:utf-8 -*-
# @atime    : 2020/11/9 2:46 下午
"""
swap nodes in pairs
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        cur = head
        head = cur.next
        cur.next = self.swapPairs(head.next)
        head.next = cur
        return head

    def swap_pairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        first = ListNode(0)
        first.next = head
        p = first
        while p.next and p.next.next:
            temp = p.next.next
            p.next.next = temp.next
            temp.next = p.next
            p.next = temp
            p = p.next.next
        return first.next


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    node_ls = [ListNode(i) for i in a]
    head = ''
    for i in range(len(node_ls)-1):
        node = node_ls[i]
        node.next = node_ls[i+1]
        if not head:
            head = node

    so = Solution()
    so.swap_pairs(head)
