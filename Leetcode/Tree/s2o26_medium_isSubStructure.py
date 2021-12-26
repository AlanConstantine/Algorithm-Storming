# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-26 14:10:05

# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

# B是A的子结构， 即 A中有出现和B相同的结构和节点值。

# 例如:
# 给定的树 A:

#      3
#     / \
#    4   5
#   / \
#  1   2
# 给定的树 B：

#    4 
#   /
#  1
# 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

# 示例 1：

# 输入：A = [1,2,3], B = [3,1]
# 输出：false
# 示例 2：

# 输入：A = [3,4,5,1,2], B = [4,1]
# 输出：true

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
from _typeshed import Self


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A and not B:
            return False
        if not A or not B:
            return False
        self.res = False

        def dfs(A, B):
            if not B:
                return True
            if not A:
                return False
            return B.val == A.val and dfs(A.left, B.left) and dfs(A.right, B.right)

        def help(root):
            if not root:
                return None
            if root.val == B.val:
                self.res = dfs(root, B)
            help(root.left)
            help(root.right)

        help(A)
        return self.res


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        result = False
        if A and B:
            if A.val == B.val:  # 递归查找匹配入口
                result = self.comp(A, B)
            if not result:  # 利用判断节省递归时间
                result = self.isSubStructure(A.left, B)
            if not result:
                result = self.isSubStructure(A.right, B)
        return result

    def comp(self, A, B):
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.comp(A.left, B.left) and self.comp(A.right, B.right)


a = TreeNode(1)
b = TreeNode(0)
c = TreeNode(1)
d = TreeNode(-4)
e = TreeNode(-3)

f = TreeNode(1)
g = TreeNode(-4)

a.left = b
a.right = c
b.left = d
b.right = e

f.left = g
print(Solution().isSubStructure(a, f))
