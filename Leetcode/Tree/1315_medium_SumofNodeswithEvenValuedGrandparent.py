# 给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：

# 该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
# 如果不存在祖父节点值为偶数的节点，那么返回 0 。


# Definition for a binary tree node.

def inorder(root):
    res = []
    if root:
        res += inorder(root.left)
        res.append(root.val)
        res += inorder(root.right)
    return res


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    sum_ = []

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.help(root)
        return sum([i.val if i else 0 for i in self.sum_])

    def help(self, root):
        if root:
            if root.val % 2 == 0:
                if root.left:
                    self.sum_.append(root.left.left)
                    self.sum_.append(root.left.right)
                if root.right:
                    self.sum_.append(root.right.left)
                    self.sum_.append(root.right.right)
            self.help(root.left)
            self.help(root.right)


class Solution:
    sum_ = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.dfs(root, None, None)
        return self.sum_

    def dfs(self, cur, parent, grandparent):
        # 利用带祖父节点的深度优先搜索
        if cur:
            if grandparent and grandparent.val % 2 == 0:
                self.sum_ += cur.val
            self.dfs(cur.left, cur, parent)
            self.dfs(cur.right, cur, parent)


a = TreeNode(6)
b = TreeNode(7)
c = TreeNode(2)
d = TreeNode(9)
e = TreeNode(7)
f = TreeNode(1)
g = TreeNode(4)
h = TreeNode(8)
i = TreeNode(1)
j = TreeNode(3)
k = TreeNode(5)

a.left = b
a.right = h
b.left = c
b.right = e
c.left = d
e.left = f
e.right = g
h.left = f
h.right = j
j.right = k

tt = TreeNode(1)

print(inorder(a))
print(Solution().sumEvenGrandparent(a))
