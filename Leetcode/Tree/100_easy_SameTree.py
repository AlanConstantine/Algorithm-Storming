# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)
        else:
            return False


p1 = TreeNode(1)
p12 = TreeNode(2)
p12 = None

p13 = TreeNode(4)
p1.left = p12
p1.right = p13

p2 = TreeNode(1)
p22 = TreeNode(2)
p23 = TreeNode(3)
p2.left = p22
p2.right = p23


S = Solution()
print(S.isSameTree(p1, p2))
