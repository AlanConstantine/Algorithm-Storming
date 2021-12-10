# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-09 10:17:28

# 设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

# 如果指定节点没有对应的“下一个”节点，则返回null。

# 示例 1:

# 输入: root = [2,1,3], p = 1

#   2
#  / \
# 1   3

# 输出: 2
# 示例 2:

# 输入: root = [5,3,6,2,4,null,null,1], p = 6

#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1

# 输出: null

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/successor-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root or not p:
            return None

        self.ans = None

        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            if root.val > p.val and not self.ans:
                self.ans = root
                return
            dfs(root.right)

        dfs(root)
        return self.ans


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        result = root
        while root:
            if root.val > p.val:
                result = root
                root = root.left
            else:
                root = root.right
        return result if result.val > p.val else None


a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(6)
d = TreeNode(2)
e = TreeNode(1)
f = TreeNode(4)

a.left = b
a.right = c
b.left = d
b.right = f
d.left = e

print(Solution().inorderSuccessor(a, f).val)
