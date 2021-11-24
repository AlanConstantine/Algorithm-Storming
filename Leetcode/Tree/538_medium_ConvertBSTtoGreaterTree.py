# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-24 09:31:59

# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

# 提醒一下，二叉搜索树满足下列约束条件：

# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum = 0

    def convertBST(self, root):
        if root:
            root.right = self.convertBST(root.right)
            self.sum += root.val
            root.val = self.sum
            root.left = self.convertBST(root.left)
        return root
