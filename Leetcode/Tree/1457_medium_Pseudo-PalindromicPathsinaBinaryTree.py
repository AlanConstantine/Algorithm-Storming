# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-05 13:05:19

# 给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

# 请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.ans = 0
        # self.s = []
        self.d = {}
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root:
            return
        # self.s.append(root.val)
        self.add(root.val)

        if not root.left and not root.right:
            if self.check():
                self.ans += 1
            self.sub(root.val)
            return
        self.dfs(root.left)
        self.dfs(root.right)
        self.sub(root.val)

    def add(self, val):
        if val in self.d:
            v = self.d[val]
            self.d[val] = v+1
        else:
            self.d[val] = 1

    def sub(self, val):
        if val in self.d:
            v = self.d[val]
            self.d[val] = v-1

    def check(self):
        odds = 0
        for k, v in self.d.items():
            if v % 2 != 0:
                odds += 1
            if odds >= 2:
                return False
        return True
