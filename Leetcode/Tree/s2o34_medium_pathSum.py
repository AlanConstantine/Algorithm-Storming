# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-12-09 12:42:12


# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

# 叶子节点 是指没有子节点的节点。

#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int):
        self.ans = []
        self.sum = 0
        if not root:
            return self.ans

        self.path = []

        def dfs(root):
            if not root:
                return None
            self.sum += root.val
            self.path.append(root.val)
            if not root.left and not root.right and self.sum == target:
                self.ans.append(self.path.copy())
                self.path.pop()
                self.sum -= root.val
                return
            dfs(root.left)
            dfs(root.right)
            self.path.pop()
            self.sum -= root.val
        dfs(root)
        return self.ans
