# Definition for a binary tree node.

# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

# 假设二叉树中至少有一个节点。

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


# 注意：最左边不代表是左子树
# 利用层序遍历访问每一层节点，并用一个变量记录访问的每一层的第一个节点
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return root.val
        s = [root]
        targ = None
        while len(s) != 0:
            s_tmp = []
            for i in range(len(s)):
                if i == 0:
                    targ = s[i].val
                if s[i].left:
                    s_tmp.append(s[i].left)
                if s[i].right:
                    s_tmp.append(s[i].right)
            s = s_tmp
        return targ


a = TreeNode(2)
b = TreeNode(1)
c = TreeNode(3)

a.left = b
a.right = c

a1 = TreeNode(1)
b1 = TreeNode(2)
c1 = TreeNode(3)
d1 = TreeNode(4)
e1 = TreeNode(5)
f1 = TreeNode(6)
g1 = TreeNode(7)

a1.left = b1
a1.right = c1
b1.left = d1
c1.left = e1
c1.right = f1
e1.left = g1

a2 = TreeNode(0)
b2 = TreeNode(-1)
a2.right = b2

print(inorder(a))
print(inorder(a1))
print(Solution().findBottomLeftValue(a2))
