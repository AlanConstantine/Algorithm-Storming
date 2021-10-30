# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-10-29 14:22:50

# Definition for a binary tree node.

# 给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。

# 进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/recover-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 中序遍历，判断是否升序，用一个指针pre记录前一个节点，然后判断pre和当前节点的大小来判断是否升序
# 两种顺序错误情况：第一种两个错误的位置相邻（1，3，2，4），第二种两个错误的位置不相邻（1，4，3，2）

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
