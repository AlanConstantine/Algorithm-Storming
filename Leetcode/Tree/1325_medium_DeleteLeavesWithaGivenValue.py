# 给你一棵以 root 为根的二叉树和一个整数 target ，请你删除所有值为 target 的 叶子节点 。

# 注意，一旦删除值为 target 的叶子节点，它的父节点就可能变成叶子节点；如果新叶子节点的值恰好也是 target ，那么这个节点也应该被删除。

# 也就是说，你需要重复此过程直到不能继续删除。

# https://leetcode-cn.com/problems/delete-leaves-with-a-given-value/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 中序遍历带节点的返回可以重构并返回到根节点
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root:
            root.left = self.removeLeafNodes(root.left, target)  # 重构左子树
            root.right = self.removeLeafNodes(root.right, target)  # 重构右子树
            if not root.left and not root.right and root.val == target:
                return None  # 如果节点值等于target且为叶子节点，直接返回None，使其父节点的其中一个子节点为None
            return root  # 否则返回当前节点
        return None


a = TreeNode(2)
b = TreeNode(2)
c = TreeNode(2)

a.left = b
a.right = c

print(Solution().removeLeafNodes(a, 2))
