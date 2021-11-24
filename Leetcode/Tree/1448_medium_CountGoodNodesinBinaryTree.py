# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-24 09:37:05

# 给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。

# 「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。
# https://leetcode-cn.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.s = []  # 利用栈存储访问过的节点，先进后出
        self.ans = 0  # 记录符合要求的节点个数

        def dfs(root):
            if root:
                self.s.append(root.val)  # 中序遍历，被访问的节点依次入栈
                dfs(root.left)  # 进入左节点
                if len(self.s) != 0 and root.val >= max(self.s):
                    self.ans += 1  # 对比栈内的节点最大值
                dfs(root.right)  # 对比结束后进入右节点
                self.s.pop()  # 当前节点的左右节点对比结束后，取出该节点

        dfs(root)
        return self.ans


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        # 利用前序遍历且只能前序遍历在这个方法上
        # 用maxvalue记录访问过的最大值

        def dfs(root, maxvalue):
            if root:
                if root.val >= maxvalue:
                    self.ans += 1
                    maxvalue = root.val  # maxvalue的仅可以向子节点传递，但是子节点的maxvalue是不会向父节点传递如果不返回的话
                dfs(root.left, maxvalue)
                dfs(root.right, maxvalue)

        dfs(root, -1e9)
        return self.ans


a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(1)
f = TreeNode(5)

a.left = b
a.right = d
b.left = c
d.left = e
d.right = f

print(Solution().goodNodes(a))
