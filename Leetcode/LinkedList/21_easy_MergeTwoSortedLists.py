# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-16 23:23:14

# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

# 示例：

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        newl = head
        while l1 != None and l2 != None:
            if l1.val >= l2.val:
                newl.next = l2
                newl = newl.next
                l2 = l2.next
            else:
                newl.next = l1
                newl = newl.next
                l1 = l1.next
        if l1 != None:
            newl.next = l1
        if l2 != None:
            newl.next = l2
        return head.next
