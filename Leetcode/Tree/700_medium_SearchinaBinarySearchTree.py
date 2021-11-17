# 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

# 例如，

# 给定二叉搜索树:

#         4
#        / \
#       2   7
#      / \
#     1   3

# 和值: 2
# 你应该返回如下子树:

#       2
#      / \
#     1   3
# 在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    # 中序遍历判断，没有利用BST的优势
    res = None
    val = None

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        self.val = val

        def help(root):
            if root:
                if root.val == self.val:
                    self.res = root
                    return
                help(root.left)
                help(root.right)
        help(root)
        return self.res


class Solution:

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        if root.val == val:  # 如果相等，则返回
            return root
        if val < root.val:  # 如果目标值小于当前节点值，说明目标值只存在当前节点的左子树上，不可能存在右子树上的
            # 所以只需要递归左子树即可
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)


a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(7)
d = TreeNode(1)
e = TreeNode(3)
a.left = b
a.right = c
b.left = d
b.right = e


print(Solution().searchBST(a, 2).val)
