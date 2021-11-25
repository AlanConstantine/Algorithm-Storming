# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-25 12:10:58


# 给你一个有根节点的二叉树，找到它最深的叶节点的最近公共祖先。

# 回想一下：

# 叶节点 是二叉树中没有子节点的节点
# 树的根节点的 深度 为 0，如果某一节点的深度为 d，那它的子节点的深度就是 d+1
# 如果我们假定 A 是一组节点 S 的 最近公共祖先，S 中的每个节点都在以 A 为根节点的子树中，且 A 的深度达到此条件下可能的最大值。

# 来源：力扣（LeetCode）
# 链接：https: // leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root):
        if not root:
            return 0

        def dfs(root):  # 利用深搜找出一棵树的最大深度
            if not root:
                return 0
            return 1+max(dfs(root.left), dfs(root.right))

        leftdepth = dfs(root.left)  # 判断左子树深度
        rightdepth = dfs(root.right)  # 判断右子树深度
        if leftdepth == rightdepth:  # 如果左子树深度==右子树深度，则当前节点为目标值
            return root
        elif leftdepth > rightdepth:  # 如果左子树大于右子树深度，说明目标节点在左子树上
            return self.lcaDeepestLeaves(root.left)
        else:  # 否则在左子树上
            return self.lcaDeepestLeaves(root.right)
