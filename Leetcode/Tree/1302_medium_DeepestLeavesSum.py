# Definition for a binary tree node.


def preorder(root):
    res = []
    if root:
        res.append(root.val)
        res += preorder(root.left)
        res += preorder(root.right)
    return res


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_level = 0
    sum_ = 0

    def deepestLeavesSum(self, root):
        self.helper(root, 0)
        return self.sum_

    def helper(self, root, level):
        if root:
            if level > self.max_level:
                self.max_level = level
                self.sum_ = root.val
            elif level == self.max_level:  # 当遍历到最大层时，相加val
                self.sum_ += root.val
            self.helper(root.left, level+1)  # 记录遍历了第几层
            self.helper(root.right, level+1)


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)

a.left = b
a.right = c
b.left = d
b.right = e
d.left = g
c.left = f
f.left = h

print(preorder(a))
print(Solution().deepestLeavesSum(a))
