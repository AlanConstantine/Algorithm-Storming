# 给定一个二叉树，计算 整个树 的坡度 。

# 一个树的 节点的坡度 定义即为，该节点左子树的节点之和和右子树节点之和的 差的绝对值 。如果没有左子树的话，左子树的节点之和为 0 ；没有右子树的话也是一样。空结点的坡度是 0 。

# 整个树 的坡度就是其所有节点的坡度之和。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 0

    def findTilt(self, root: TreeNode) -> int:

        def help(root):
            if root:
                vall = help(root.left)  # 左节点子树和
                valr = help(root.right)  # 右节点子树和
                self.res += abs(vall-valr)  # 计算坡度，并累加到结果上
                return vall + valr + root.val  # 返回当前节点值+当前节点所有子树值的和
            return 0
        help(root)
        return self.res


def inorder(root):
    res = []
    if root:
        res += inorder(root.left)
        res.append(root.val)
        res += inorder(root.right)
    return res


a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(9)
d = TreeNode(3)
e = TreeNode(5)
f = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(inorder(a))
res = Solution().findTilt(a)
print(res)
