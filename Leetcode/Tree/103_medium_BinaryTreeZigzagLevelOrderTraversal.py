# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-28 13:51:11

# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层序遍历如下：

# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []

        res = []
        s = [root]
        depth = 1
        while s:
            stmp = []
            if depth % 2 == 0:
                subres = [n.val for n in s[::-1]]
            else:
                subres = [n.val for n in s]
            res.append(subres)
            for n in s:
                if n.left:
                    stmp.append(n.left)
                if n.right:
                    stmp.append(n.right)
            s = stmp
            depth += 1
        return res
