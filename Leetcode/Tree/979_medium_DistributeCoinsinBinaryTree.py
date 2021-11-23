# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-23 15:13:48


# 给定一个有 N 个结点的二叉树的根结点 root，树中的每个结点上都对应有 node.val 枚硬币，并且总共有 N 枚硬币。

# 在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。(移动可以是从父结点到子结点，或者从子结点移动到父结点。)。

# 返回使每个结点上只有一枚硬币所需的移动次数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/distribute-coins-in-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0

        def dfs(root):
            if not root:
                return 0
            leftneed = dfs(root.left)
            rightneed = dfs(root.right)
            self.ans += abs(leftneed) + abs(rightneed)
            return leftneed + rightneed + (root.val - 1)

        dfs(root)
        return self.ans
