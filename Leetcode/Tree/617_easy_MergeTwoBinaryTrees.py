# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

# 示例 1:

# 输入:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# 输出:
# 合并后的树:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
# 注意: 合并必须从两个树的根节点开始。


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
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        resval1, resval2 = 0, 0
        pl1, pr1, pl2, pr2 = None, None, None, None
        if root1:
            resval1 = root1.val
            pl1 = root1.left
            pr1 = root1.right
        if root2:
            resval2 = root2.val
            pl2 = root2.left
            pr2 = root2.right
        if not root1 and not root2:
            return None
        merg_root = TreeNode(resval1+resval2)
        merg_root.left = self.mergeTrees(pl1, pl2)
        merg_root.right = self.mergeTrees(pr1, pr2)
        return merg_root


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 or not root2:  # 只在同一棵树上操作，当其中有棵树为None时，直接返回非None的那个树，或者都是None的时候就返回None
            return root1 if root1 else root2
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


a = TreeNode(1)
b = TreeNode(3)
c = TreeNode(2)
d = TreeNode(5)
a.left = b
a.right = c
b.left = d

e = TreeNode(2)
f = TreeNode(1)
g = TreeNode(3)
h = TreeNode(4)
i = TreeNode(7)
e.left = f
e.right = g
f.right = h
g.right = i


print(inorder(a))
print(inorder(e))
print(inorder(Solution().mergeTrees(a, e)))
