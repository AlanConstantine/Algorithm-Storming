# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-20 18:52:33


# 给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：

# 选择二叉树中 任意 节点和一个方向（左或者右）。
# 如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
# 改变前进方向：左变右或者右变左。
# 重复第二步和第三步，直到你在树中无法继续移动。
# 交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。

# 请你返回给定树中最长 交错路径 的长度。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-zigzag-path-in-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# Reference: https://leetcode-cn.com/problems/longest-zigzag-path-in-a-binary-tree/solution/dfsduan-duan-ba-xing-dai-ma-you-ya-jie-j-kfyz/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return None
        self.max_path = 0

        def dfs(root, l, r):
            if not root:
                return
            self.max_path = max(l, r, self.max_path)
            if root.left:
                dfs(root.left, r+1, 0)
            if root.right:
                dfs(root.right, 0, l+1)

        dfs(root, 0, 0)
        return self.max_path


a = TreeNode(1)
b = TreeNode(1)
c = TreeNode(1)
d = TreeNode(1)
e = TreeNode(1)
f = TreeNode(1)
g = TreeNode(1)
h = TreeNode(1)

a.right = b
b.left = c
b.right = d
d.left = e
d.right = f
e.left = g
g.left = h

print(Solution().longestZigZag(a))
