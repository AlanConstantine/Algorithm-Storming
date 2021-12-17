# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-17 14:17:41

# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

# 叶子节点 是指没有子节点的节点。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False

        self.s = 0
        self.flag = False

        def dfs(root):
            if not root or self.flag:
                return
            self.s += root.val
            if not root.left and not root.right:
                if self.s == targetSum:
                    self.flag = True
                    return
            dfs(root.left)
            dfs(root.right)
            self.s -= root.val
        dfs(root)
        return self.flag


a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(11)
d = TreeNode(7)
e = TreeNode(2)
f = TreeNode(8)

a.left = b
a.right = f
b.left = c
c.left = d
c.right = e

print(Solution().hasPathSum(a, 22))
