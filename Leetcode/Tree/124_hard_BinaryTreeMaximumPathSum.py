# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-26 16:36:56

# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

# 路径和 是路径中各节点值的总和。

# 给你一个二叉树的根节点 root ，返回其 最大路径和 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root) -> int:
        self.res = float("-inf")
        if not root:
            return 0

        def dfs(root):
            if not root:
                return 0
            # 与0对比的原因是，如果当其左子树的路径最大和比0还小，则路径就可以不考虑往左子树走
            L = max(dfs(root.left), 0)
            R = max(dfs(root.right), 0)  # 与左子树同理
            # 情况一：左子树返回的路径最大
            # 情况二：右子树返回的路径最大
            # 情况三：过节点连接左右子树的路径最大，则这个路径要对比的是被过的节点的上一个节点的左右子树路径
            # 如果是情况三，那么就判定pass_路径与当前最大结果对比，因为如果选了情况三，则对比时当前节点不需要再与其父节点组成的路径进行对比，仅考虑全局对比
            # 总体思路就是，对比每一个节点左右子树的路径，以及每一个节点的过节点路径
            #    -10
            #    / \
            #   9  20
            #     /  \
            #    15   7
            # 15 -> 20 -> 7就是过节点路径
            pass_ = L + R + root.val
            self.res = max(self.res, pass_)
            return root.val + max(L, R)  # 返回当前节点为根节点时候的最大值

        dfs(root)
        return self.res


a = TreeNode(-13)
print(Solution().maxPathSum(a))
