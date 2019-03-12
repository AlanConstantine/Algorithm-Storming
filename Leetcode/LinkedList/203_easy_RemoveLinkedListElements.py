# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-06 03:03:04

# 删除链表中等于给定值 val 的所有节点。

# 示例:

# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def removeElements(self, head, val):
#         """
#         :type head: ListNode
#         :type val: int
#         :rtype: ListNode
#         """
#         if head.val == val:
#             head.val = head.next.val
#             head.next = head.next.next
#         while head.next:
#             if head.next.val == val:
#                 head.next = head.next.next
#             else:
#                 head = head.next
#         return head


class SolutionII(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head


n1 = ListNode(6)
n2 = ListNode(6)
n3 = ListNode(6)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(6)
n7 = ListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

s = Solution()
s.removeElements(n1, 6)
print(n1.val)
