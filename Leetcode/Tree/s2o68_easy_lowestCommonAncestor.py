# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-26 13:21:09

# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        pval = p.val
        qval = q.val
        if pval > q.val:
            pval, qval = qval, pval
        self.ans = None

        def dfs(root, pval, qval):
            if not root:
                return None
            if root.val >= pval and root.val <= qval:
                self.ans = root
                return
            dfs(root.left, pval, qval)
            dfs(root.right, pval, qval)

        dfs(root, pval, qval)
        return self.ans
