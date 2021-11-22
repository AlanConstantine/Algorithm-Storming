# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-22 13:32:31

# 给定一个二叉搜索树的 根节点 root 和一个整数 k , 请判断该二叉搜索树中是否存在两个节点它们的值之和等于 k 。假设二叉搜索树中节点的值均唯一。

#  

# 示例 1：

# 输入: root = [8,6,10,5,7,9,11], k = 12
# 输出: true
# 解释: 节点 5 和节点 7 之和等于 12
# 示例 2：

# 输入: root = [8,6,10,5,7,9,11], k = 22
# 输出: false
# 解释: 不存在两个节点值之和为 22 的节点

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/opLdQZ
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        self.diffs = set()

        def dfs(root, k):
            if not root:
                return False
            if root.val in self.diffs:
                return True
            self.diffs.add(k - root.val)
            return dfs(root.left, k) or dfs(root.right, k)
        return dfs(root, k)
