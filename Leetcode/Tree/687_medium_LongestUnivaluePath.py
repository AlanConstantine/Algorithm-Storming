# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-23 10:40:42

# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

# 注意：两个节点之间的路径长度由它们之间的边数表示。

# 示例 1:

# 输入:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# 输出:

# 2
# 示例 2:

# 输入:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# 输出:

# 2

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-univalue-path
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.maxpath = -1e9

        def dfs(root):
            if not root:
                return 0
            leftc = dfs(root.left)  # 获取左树结果
            rightc = dfs(root.right)  # 获取右树结果
            if root.left and root.left.val == root.val:
                leftc += 1  # 若左树值等于当前节点，左树加一
            else:
                leftc = 0  # 否则左树归0
            if root.right and root.right.val == root.val:
                rightc += 1
            else:
                rightc = 0
            self.maxpath = max(self.maxpath, leftc+rightc)  # maxpath记录最大结果值
            return max(leftc, rightc)

        dfs(root)
        return self.maxpath


a = TreeNode(1)
b = TreeNode(4)
c = TreeNode(5)
a.left = b
a.right = c
d = TreeNode(4)
e = TreeNode(4)
f = TreeNode(5)
b.left = d
b.right = e
c.right = f

print(Solution().longestUnivaluePath(a))
