# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-20 19:34:14

# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

# 一般来说，删除节点可分为两个步骤：

# 首先找到需要删除的节点；
# 如果找到了，删除它。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        def dfs(root):
            if not root:
                return None
            # 在BST中查找目标值的时候要善用BST的特点以节省检索时间
            if root.val > key:  # 当当前值大于key，说明key肯定只存在于当前节点的左节点
                root.left = dfs(root.left)
            elif root.val < key:  # 当当前值小于key，说明key肯定只存在于当前节点的右节点
                root.right = dfs(root.right)
            else:  # 否则当当前节点等于key时，分三种情况讨论
                if not root.left:  # 当不存在左节点的时候
                    return root.right  # 用右节点替代当前节点
                if not root.right:  # 当不存在右节点的时候
                    return root.left  # 用左节点替代当前节点
                # 当同时存在左右节点的时候
                node = root.right  # 要将左节点放在右节点的最左节点
                while node.left:
                    node = node.left
                node.left = root.left
                root = root.right  # 再继续用右节点替代当前节点
            return root

        return dfs(root)
