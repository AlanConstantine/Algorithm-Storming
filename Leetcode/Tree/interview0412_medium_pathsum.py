# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-22 19:09:08

# 给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

# 示例:
# 给定如下二叉树，以及目标和 sum = 22，

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:

# 3
# 解释：和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/paths-with-sum-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Reference: https://leetcode-cn.com/problems/paths-with-sum-lcci/solution/yi-pian-wen-zhang-jie-jue-suo-you-er-cha-w3hu/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.res = 0

        def dfs(root):
            if not root:
                return
            getsum(root, 0)
            dfs(root.left)
            dfs(root.right)

        def getsum(root, s):
            if not root:
                return
            s += root.val
            if s == sum:
                self.res += 1
                # 注意不要return,因为不要求到叶节点结束,所以一条路径下面还可能有另一条
            getsum(root.left, s)
            getsum(root.right, s)

        dfs(root)
        return self.res


class Solution:
    res = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.dfs(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.res

    def dfs(self, root, sum):
        if not root:
            return
        sum -= root.val
        if sum == 0:
            self.res += 1
        self.dfs(root.left, sum)
        self.dfs(root.right, sum)


#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1


a = TreeNode(1)
b = TreeNode(-2)
c = TreeNode(-3)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(-2)
g = TreeNode(-1)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
d.left = g
print(Solution().pathSum(a, -1))
