# 给定一个二叉搜索树，请将它的每个节点的值替换成树中大于或者等于该节点值的所有节点值之和。

#  

# 提醒一下，二叉搜索树满足下列约束条件：

# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。

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

# 正常的中序遍历在BST是单调递增的左中右遍历节点，可以使用逆中序遍历变成单调递减的右中左进行遍历，边遍历边累加节点值


class Solution:
    add = 0

    def convertBST(self, root):
        if root:
            self.convertBST(root.right)
            root.val += self.add
            self.add = root.val
            self.convertBST(root.left)
        return root


a = TreeNode(4)
b = TreeNode(1)
c = TreeNode(0)
d = TreeNode(2)
e = TreeNode(3)
f = TreeNode(6)
g = TreeNode(5)
h = TreeNode(7)
i = TreeNode(8)

a.left = b
a.right = f
b.left = c
b.right = d
d.right = e
f.left = g
f.right = h
h.right = i

print(inorder(a))
