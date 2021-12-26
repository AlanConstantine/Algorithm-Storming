# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-26 17:35:44

# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

# 路径和 是路径中各节点值的总和。

# 给定一个二叉树的根节点 root ，返回其 最大路径和，即所有路径上节点值之和的最大值。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/jC7MId
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = float('-inf')

        def dfs(root):
            if not root:
                return 0
            leftgain = max(0, dfs(root.left))
            rightgain = max(0, dfs(root.right))
            pass_current_node_gain = leftgain + rightgain + root.val
            self.max = max(self.max, pass_current_node_gain)
            return root.val + max(leftgain, rightgain)

        dfs(root)
        return self.max
