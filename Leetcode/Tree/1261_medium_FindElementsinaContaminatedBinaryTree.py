# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-21 09:00:25

# 给出一个满足下述规则的二叉树：

# root.val == 0
# 如果 treeNode.val == x 且 treeNode.left != null，那么 treeNode.left.val == 2 * x + 1
# 如果 treeNode.val == x 且 treeNode.right != null，那么 treeNode.right.val == 2 * x + 2
# 现在这个二叉树受到「污染」，所有的 treeNode.val 都变成了 -1。

# 请你先还原二叉树，然后实现 FindElements 类：

# FindElements(TreeNode* root) 用受污染的二叉树初始化对象，你需要先把它还原。
# bool find(int target) 判断目标值 target 是否存在于还原后的二叉树中并返回结果。

# 来源：力扣（LeetCode）
# 链接：https: // leetcode-cn.com/problems/find-elements-in-a-contaminated-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: TreeNode):
        self.ser = []
        if not root:
            return None

        root.val = 0

        def help(root):
            if root:
                self.ser.append(root.val)
                if root.left:
                    root.left.val = 2 * root.val + 1
                if root.right:
                    root.right.val = 2 * root.val + 2
                root.left = help(root.left)
                root.right = help(root.right)
                return root
            return root

        recoverroot = help(root)

    def find(self, target: int) -> bool:
        return target in self.ser

        # Your FindElements object will be instantiated and called as such:
        # obj = FindElements(root)
        # param_1 = obj.find(target)


def inorder(root):
    res = []
    if root:
        res += inorder(root.left)
        res.append(root.val)
        res += inorder(root.right)
    return res


a = TreeNode(-1)
b = TreeNode(-1)
c = TreeNode(-1)
d = TreeNode(-1)
e = TreeNode(-1)

a.left = b
a.right = c
b.left = d
b.right = e

s = FindElements(a)
# print(inorder(s))
