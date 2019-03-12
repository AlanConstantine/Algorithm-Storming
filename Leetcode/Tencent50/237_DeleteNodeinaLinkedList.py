# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-05 17:28:01
# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

# 现有一个链表 -- head = [4,5,1,9]，它可以表示为:


# 示例 1:

# 输入: head = [4,5,1,9], node = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
# 示例 2:

# 输入: head = [4,5,1,9], node = 1
# 输出: [4,5,9]
# 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# 这道题出的很骚气，实际上不需要将指定节点的下一个对象链接上指定节点的上一个对象，直接对当前指定节点的val进行修改成
# 下一个节点的值，将next指向下一个节点的next，达到删除节点的效果，但是实际上从内存来说，这个指定的节点并没有
# 被删除，只是被修改了val和next而已，其内存地址没有变。


head = [4, 5, 1, 9]
n = ListNode(head[0])
first = n
for i in range(1, len(head)):
    n.next = ListNode(head[i])
    n = n.next

print(first.val)
print(first.next.val)
second = first.next
print(second.next.val)
thrid = second.next
print(thrid.next.val)
