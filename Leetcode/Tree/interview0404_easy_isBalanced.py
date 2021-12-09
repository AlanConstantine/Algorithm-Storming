# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-12-09 12:18:26

# 实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。


# 示例 1:
# 给定二叉树 [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。
# 示例 2:
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#       1
#      / \
#     2   2
#    / \
#   3   3
#  / \
# 4   4
# 返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/check-balance-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.ans = True

        def dfs(root):
            if not root:
                return 0
            L = dfs(root.left)
            R = dfs(root.right)
            if abs(L-R) > 1:
                self.ans = False
            return max(L, R) + 1
        dfs(root)
        return self.ans
