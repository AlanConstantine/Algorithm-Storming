# NC78 反转链表
# link: https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=117&&tqId=37777&rp=1&ru=/ta/job-code-high&qru=/ta/job-code-high/question-ranking
# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        cur = pHead  # current node
        nex = None  # next node
        pre = None  # pre node
        while cur:
            nex = cur.next  # get the next node
            cur.next = pre  # set the current node.next to pre
            pre = cur  # set current to the pre node
            # set the next node to the current node and enter to next loop.
            cur = nex
        return pre


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

n1.next = n2
n2.next = n3

s = Solution()
newHead = s.ReverseList(pHead=n1)
print(newHead.val)
print(newHead.next.val)
print(newHead.next.next.val)
