# https://leetcode-cn.com/problems/find-bottom-left-tree-value/
# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

# 假设二叉树中至少有一个节点。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root) -> int:
        s = [root]
        while s:
            res = s[0]
            for i in range(len(s)):
                n = s.pop(0)
                if n.left:
                    s.append(root.left)
                if n.right:
                    s.append(root.right)
            if not s:
                return res.val
