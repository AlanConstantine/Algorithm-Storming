# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-23 14:43:53

# 实现一个函数，检查一棵二叉树是否为二叉搜索树。

# 示例 1:
# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/legal-binary-search-tree-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        self.pre = None
        self.res = True

        def dfs(root):
            if not root:
                return True
            dfs(root.left)

            if self.pre != None and root.val <= self.pre:
                self.res = False
            self.pre = root.val
            dfs(root.right)

        dfs(root)
        return self.res


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root, mi, ma):
            if not root:
                return True
            if root.val <= mi or root.val >= ma:
                return False
            return dfs(root.left, mi, root.val) and dfs(root.right, root.val, ma)
        return dfs(root, -float("inf"), float("inf"))


a = TreeNode(0)
# b = TreeNode(1)
c = TreeNode(-1)

# a.left = b
a.right = c
print(Solution().isValidBST(a))
