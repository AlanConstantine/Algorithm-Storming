# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-23 13:27:13

# 设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。

# 例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]

#     3
#    / \
#   5   1
#  / \ / \
# 6  2 0  8
#   / \
#  7   4
# 示例 1:

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 示例 2:

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
# 说明:

# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/first-common-ancestor-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 思路：利用深度搜索，判断两个节点是否存在当前节点的子树当中，如果存在则说明当前节点就是目标节点
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        self.ans = None

        def dfs(root, p, q):
            if not root:
                return False
            if root.val == p.val or root.val == q.val:
                self.ans = root  # 这一步是为了保证当前节点可能也满足条件，即自己也可以是自己的父节点
                return True
            rootleftres = dfs(root.left, p, q)
            rootrightres = dfs(root.right, p, q)
            if rootleftres and rootrightres:
                self.ans = root
            else:
                return rootrightres or rootleftres

        dfs(root, p, q)
        return self.ans
