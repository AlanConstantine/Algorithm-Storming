# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-28 19:33:40

# 给定二叉树的根节点 root，找出存在于 不同 节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。

# （如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-difference-between-node-and-ancestor
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return None
        self.s = []
        self.ans = -1e9

        def dfs(root):
            if not root:
                return None
            self.s.append(root.val)
            if not root.left and not root.right:
                self.ans = max(self.ans, max(self.s)-min(self.s))
                self.s.pop()
                return
            dfs(root.left)
            dfs(root.right)
            self.s.pop()

        dfs(root)
        return self.ans
