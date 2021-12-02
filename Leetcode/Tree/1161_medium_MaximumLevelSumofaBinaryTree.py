# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-02 13:33:21

# 给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。

# 请你找出层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-level-sum-of-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        ans = []
        if not root:
            return None
        s = [root]
        depth = 1
        ans = 0
        maxsum = -1e9
        while s:
            levelsum = 0
            stmp = []
            for n in s:
                levelsum += n.val
                for each in (n.left, n.right):
                    if each:
                        stmp.append(each)
            if levelsum > maxsum:
                ans = depth
                maxsum = levelsum
            depth += 1

            s = stmp
        return ans
