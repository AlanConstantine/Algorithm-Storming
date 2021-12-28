# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-12-28 09:44:38

# 给定一棵二叉树的根 root，请你考虑它所有 从根到叶的路径：从根到任何叶的路径。（所谓一个叶子节点，就是一个没有子节点的节点）

# 假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为「不足节点」，需要被删除。

# 请你删除所有不足节点，并返回生成的二叉树的根。

#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/insufficient-nodes-in-root-to-leaf-paths
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        pass
