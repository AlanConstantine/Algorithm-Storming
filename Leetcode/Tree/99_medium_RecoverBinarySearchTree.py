# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-10-29 14:22:50

# Definition for a binary tree node.

def in_traversal(root):
    s = []
    if root:
        s += in_traversal(root.left)
        s.append(root.val)
        s += in_traversal(root.right)
    return s


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def __init__(self):
    #     self.pre = None
    #     self.t1 = None
    #     self.t2 = None

    def recoverTree(self, root):
        self.pre = None
        self.t1 = None
        self.t2 = None
        self.recover(root)
        self.t1.val, self.t2.val = self.t2.val, self.t1.val

    def recover(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            self.recover(root.left)
            if not self.pre:
                self.pre = root
            else:
                if root.val < self.pre.val and not self.t2:
                    self.t1 = self.pre
                    self.t2 = root
                if root.val < self.pre.val and self.t2:
                    self.t2 = root
                self.pre = root
            self.recover(root.right)


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)

c.left = a
c.right = d
d.left = b

S = Solution()
print(in_traversal(c))
S.recoverTree(c)
print(in_traversal(c))
