# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-25 13:36:31

# 给你二叉树的根结点 root ，此外树的每个结点的值要么是 0 ，要么是 1 。

# 返回移除了所有不包含 1 的子树的原二叉树。

# 节点 node 的子树为 node 本身加上所有 node 的后代。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-pruning
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root):
        def dfs(root):
            if not root:
                return False
            l = dfs(root.left)  # 获取左子树的1存在情况
            r = dfs(root.right)  # 获取右子树1存在情况
            if not l:
                root.left = None  # 若左子树没有存在1则把当前节点的左节点置空
            if not r:
                root.right = None  # 同理右节点
            return l or r or root.val == 1  # 判断当前节点是否为1
        return root if dfs(root) else None


a = TreeNode(1)
b = TreeNode(0)
c = TreeNode(0)
d = TreeNode(1)
a.right = b
b.left = c
b.right = d


def inorder(root):
    a = []
    if root:
        a += inorder(root.left)
        a.append(root.val)
        a += inorder(root.right)
    return a


print(inorder(a))
print(inorder(Solution().pruneTree(a)))
