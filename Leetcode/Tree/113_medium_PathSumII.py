# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-05 11:35:22

# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

# 叶子节点 是指没有子节点的节点。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def pathSum(self, root, targetSum: int):
        if not root:
            return None
        self.ans = []
        s = []
        self.sum_ = 0

        def dfs(root):
            if not root:
                return
            self.sum_ += root.val
            s.append(root.val)
            if not root.left and not root.right:
                if self.sum_ == targetSum:
                    self.ans.append(s.copy())
                self.sum_ -= root.val
                s.pop()
                return
            dfs(root.left)
            dfs(root.right)
            self.sum_ -= root.val
            s.pop()

        dfs(root)
        return self.ans


class Solution:
    def pathSum(self, root, targetSum: int):
        res = []
        if root:
            if not root.left and not root.right:
                if root.val == targetSum:
                    res.append([root.val])  # 如果满足要求，则创建一个路径， 否则res为空
            else:
                leftpath = self.pathSum(
                    root.left, targetSum-root.val)  # 每次传递targnum减掉当前值
                rightpath = self.pathSum(root.right, targetSum-root.val)
                for p in leftpath:  # leftpath只有当根结点满足的时候才会有长度，否则为空
                    res.append([root.val]+p)
                for p in rightpath:
                    res.append([root.val]+p)
        return res


def inorder(root):
    res = []
    if root:
        res += inorder(root.left)
        res.append(root.val)
        res += inorder(root.right)
    return res


a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(1)
d = TreeNode(3)
e = TreeNode(7)

a.left = b
a.right = e
b.left = c
b.right = d

print(inorder(a))
print(Solution().pathSum(a, 7))
