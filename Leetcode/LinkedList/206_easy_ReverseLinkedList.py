# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-06 04:02:20

# 链表反转（递归）

# 反转一个单链表。

# 示例:

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = None
        c = head
        while c:
            temp = c.next
            c.next = p
            p = c
            c = temp
        return p


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3

print(n1.val)
print(n1.next.val)
print(n2.next.val)
print(n3.next)

s = Solution()
n = s.reverseList(n1)
# reverse(n1, None)
print('After reverse:')
# print(n4.val)
# print(n4.next.val)
# print(n3.next.val)
# print(n2.next.val)
# print(n1.next)
print(n.val)
print(n.next.val)
print(n.next.next.val)
print(n.next.next.next)
