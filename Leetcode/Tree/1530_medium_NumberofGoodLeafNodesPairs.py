# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-10 13:53:42

# 给你二叉树的根节点 root 和一个整数 distance 。

# 如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。

# 返回树中 好叶子节点对的数量 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-good-leaf-nodes-pairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root:
            return 0
        self.counter = 0

        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:  # 没有左右子节点说明当前节点为叶子结点，返回当前叶子结点对于其父节点的深度，即为1
                return [1]
            L = dfs(root.left)  # 获取左子树的叶子结点深度
            R = dfs(root.right)  # 获取右子树的叶子结点深度
            for l in L:
                for r in R:
                    if l + r <= distance:  # 遍历当前节点的所有叶子结点的深度并判断是否满足要求
                        self.counter += 1
            # 返回时把所有叶子结点的深度并接起来即返回当前结点的所有叶子结点的深度（并+1，因为要算上当前节点的）
            return [d+1 for d in L+R]

        dfs(root)
        return self.counter
