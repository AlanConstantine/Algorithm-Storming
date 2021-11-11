# 给定一棵二叉树，设计一个算法，
# 创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。
# 返回一个包含所有深度的链表的数组。


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree):
        if not tree:
            return []
        res = []
        stack = [tree]
        while len(stack) != 0:
            stack_tmp = []
            head = ListNode(0)
            pre = head
            for n in range(0, len(stack)):
                head.next = ListNode(stack[n].val)
                head = head.next
                if stack[n].left:
                    stack_tmp.append(stack[n].left)
                if stack[n].right:
                    stack_tmp.append(stack[n].right)
            stack = stack_tmp
            res.append(pre.next)
        return res


def iterlist(head):
    res = []
    if head:
        res.append(head.val)
        res += iterlist(head.next)
    return res


def inorder(root):
    res = []
    if root:
        res += inorder(root.left)
        res.append(root.val)
        res += inorder(root.right)
    return res


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)

a.left = b
a.right = c
b.left = d
b.right = e
d.left = h
c.right = g

print(inorder(a))
res = Solution().listOfDepth(a)
for i in res:
    print(iterlist(i))
