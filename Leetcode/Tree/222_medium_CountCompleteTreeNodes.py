# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

# 完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def countNodes(self, root: TreeNode) -> int:
        count = 0
        if root:
            count += 1
            count += self.countNodes(root.left)
            count += self.countNodes(root.right)
        return count


class Solution2:
    def countNodes(self, root: TreeNode) -> int:
        if root:
            return self.countNodes(root.left)+self.countNodes(root.right)+1
        else:
            return 0


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.countNodes(root.left)+self.countNodes(root.right)+1 if root else 0

# 计算层数
# private int countLevel(TreeNode root){
#     if(root == null){
#         return 0
#     }
#     return Math.max(countLevel(root.left), countLevel(root.right)) + 1
# }
