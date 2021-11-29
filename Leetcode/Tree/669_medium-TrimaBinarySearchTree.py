# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-29 09:24:11

# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。修剪树不应该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。

# 所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/trim-a-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 因为是BST，所以如果当前节点的值小于low，则说明当前节点的左子树所有节点都小于low，应该全部删除
# 同理，如果当前节点值大于high， 则说明当前节点的所有右子树都会大于high，因此右子树也可以全部删除


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None

        if root.val > high:
            return self.trimBST(root.left, low, high)
        if root.val < low:
            return self.trimBST(root.right, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root


a = TreeNode(3)
b = TreeNode(0)
c = TreeNode(4)
d = TreeNode(2)
e = TreeNode(1)
f = TreeNode(1.5)

a.left = b
a.right = c
b.right = d
d.left = e
e.right = f


def inorder(root):
    res = []
    if root:
        res += inorder(root.left)
        res.append(root.val)
        res += inorder(root.right)
    return res


print(inorder(Solution().trimBST(a, low=1, high=3)))
