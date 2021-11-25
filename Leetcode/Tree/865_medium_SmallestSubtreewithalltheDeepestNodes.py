# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-25 13:06:41

# 给定一个根为 root 的二叉树，每个节点的深度是 该节点到根的最短距离 。

# 如果一个节点在 整个树 的任意节点之间具有最大的深度，则该节点是 最深的 。

# 一个节点的 子树 是该节点加上它的所有后代的集合。

# 返回能满足 以该节点为根的子树中包含所有最深的节点 这一条件的具有最大深度的节点。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/smallest-subtree-with-all-the-deepest-nodes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return 0

        def dfs(root):
            if not root:
                return 0
            return 1+max(dfs(root.left), dfs(root.right))

        ldepth = dfs(root.left)
        rdepth = dfs(root.right)

        if ldepth == rdepth:
            return root
        elif ldepth > rdepth:
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)
