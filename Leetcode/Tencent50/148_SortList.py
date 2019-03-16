# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-16 17:17:01

# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

# 示例 1:

# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2:

# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.quick_sort(head, None)
        return head

    def swap(self, a, b):
        tmp = a.val
        a.val = b.val
        b.val = tmp

    def quick_sort(self, start, end):
        if start == end:
            return
        mid_value = start.val  # 设定基准数
        # 快慢指针和数组的快排的快慢指针有差，这里的慢指针指向基准自己，
        # 而数组的则使先指向基准的下一位，
        # 因此在互换快慢指针的时候，慢指针需要先指向下一个节点再开始换
        first = ListNode(mid_value)  # 慢指针
        first.next = start.next
        second = first.next  # 快指针
        while second != end and second != None:
            # 快指针从左向右扫，end表示快指针的范围
            if second.val <= mid_value:
                first = first.next
                # 当快指针遇到小于基准数的值时
                self.swap(second, first)
                # 快指针和慢指针互换
                # 慢指针指向下一节点，这一步相当于index+1
            second = second.next
            # 快指针指向下一节点，这一步相当于for循环的i+=1
        self.swap(first, start)
        # 最后慢指针和基准节点互换，使所有小于基准值的节点全部在基准节点左侧
        self.quick_sort(start, first)
        self.quick_sort(first.next, end)


class SolutionII(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 这个方法很骚气~
        q = head
        listnode = []
        while q:
            listnode.append(q.val)
            q = q.next
        q = head
        listnode.sort()
        le = len(listnode)
        for i in range(le):
            q.val = listnode[i]
            q = q.next
        return head


s = Solution()
n1 = ListNode(4)
n2 = ListNode(2)
n3 = ListNode(1)
n4 = ListNode(3)
n1.next = n2
n2.next = n3
n3.next = n4
s.sortList(n1)
