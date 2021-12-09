# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-09 09:36:09

# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

#  

# 示例 :
# 给定二叉树

#           1
#          / \
#         2   3
#        / \
#       4   5
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return None

        self.ans = -1e9

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)  # 返回左子树的最大深度
            r = dfs(root.right)  # 返回右子树的最大深度
            self.ans = max(self.ans, l+r)  # 对比访问过的节点的左右深度和
            return max(l, r)+1  # 当前节点的最大深度是取左右子树的最大深度+1
        dfs(root)
        return self.ans
