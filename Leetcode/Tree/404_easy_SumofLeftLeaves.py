# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-12-09 11:55:53

# 计算给定二叉树的所有左叶子之和。

# 示例：

#     3
#    / \
#   9  20
#     /  \
#    15   7

# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sum-of-left-leaves
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return ans

        s = [root]
        while s:
            size = len(s)
            for _ in range(size):
                n = s.pop(0)
                if n.left:
                    s.append(n.left)
                    if not n.left.left and not n.left.right:
                        ans += n.left.val
                if n.right:
                    s.append(n.right)
        return ans


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return res
        if root.left and not root.left.left and not root.left.right:  # 判断是否存在左节点，且左节点有无子节点
            res += root.val  # 左节点存在且没有子节点说明该左节点为左叶子节点，累加上该左节点的值
        # 递归左右子树返回结果并加上当前计算的结果
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) + res
