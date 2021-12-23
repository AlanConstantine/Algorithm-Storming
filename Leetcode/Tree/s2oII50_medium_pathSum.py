# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-23 16:50:56

# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/6eUYwP
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        self.prefix = collections.defaultdict(int)
        self.prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0
            curr += root.val

            res = self.prefix[curr-targetSum]
            self.prefix[curr] += 1
            res += dfs(root.left, curr)
            res += dfs(root.right, curr)
            self.prefix[curr] -= 1
            return res

        return dfs(root, 0)
