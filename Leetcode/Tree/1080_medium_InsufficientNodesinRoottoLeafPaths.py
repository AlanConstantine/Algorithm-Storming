# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-12-28 09:44:38

# 给定一棵二叉树的根 root，请你考虑它所有 从根到叶的路径：从根到任何叶的路径。（所谓一个叶子节点，就是一个没有子节点的节点）

# 假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为「不足节点」，需要被删除。

# 请你删除所有不足节点，并返回生成的二叉树的根。

#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/insufficient-nodes-in-root-to-leaf-paths
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    # fail: 理解错题意，只考虑了路径是否小于limit，没有考虑根叶路径的总和
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        self.sum = 0

        def dfs(root):
            if not root:
                return None
            self.sum += root.val
            if self.sum < limit:
                self.sum -= root.val
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            self.sum -= root.val
            return root

        return dfs(root)


class Solution2:
    # fail: 无法通过测试exp2
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root:
            return None

        def dfs(root, v):
            if not root:
                return False
            L = dfs(root.left, v+root.val)
            R = dfs(root.right, v+root.val)
            if L:
                root.left = None
            if R:
                root.right = None
            if not root.left and not root.right:
                return v + root.val < limit
            return False

        return None if dfs(root, 0) else root


class Solution3:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(root, sum_):
            if not root.left and not root.right:
                return root.val + sum_ < limit

            l_tree_delete = True
            r_tree_delete = True

            if root.left:
                l_tree_delete = dfs(root.left, sum_ + root.val)
            if root.right:
                r_tree_delete = dfs(root.right, sum_+root.val)
            if l_tree_delete:
                root.left = None
            if r_tree_delete:
                root.right = None
            return r_tree_delete and l_tree_delete

        return None if dfs(root, 0) else root


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root:
            return None
        if not root.left and not root.right:
            if root.val < limit:
                return None
            else:
                return root
        root.left = self.sufficientSubset(root.left, limit-root.val)
        root.right = self.sufficientSubset(root.right, limit-root.val)
        # 左右子树都为空，意味着这个子树上没有被保留的路径，那么这个结点也没有保留的必要了
        # 即删除了左右节点后新形成的叶子结点不能算作题意要求的叶子结点
        if not root.left and not root.right:
            return None
        return root


        # exp1
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
d = TreeNode(4)
e = TreeNode(7)
f = TreeNode(8)
g = TreeNode(12)
h = TreeNode(13)
i = TreeNode(14)
k = TreeNode(9)
n1 = TreeNode(-99)
n2 = TreeNode(-99)
n3 = TreeNode(-99)
n4 = TreeNode(-99)
n5 = TreeNode(-99)

b.left = d
b.right = n1
d.left = f
d.right = k
n1.left = n2
n1.right = n3
c.left = n4
c.right = e
n4.left = g
n4.right = h
e.left = n5
e.right = i
limit = 1


# exp2
# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(-3)
# d = TreeNode(-5)
# e = TreeNode(4)

# a.left = b
# a.right = c
# b.left = d
# c.left = e

# limit = -1


def inorder(root):
    res = []
    if not root:
        return res
    res += inorder(root.left)
    res.append(root.val)
    res += inorder(root.right)
    return res


# a = TreeNode(-2)

print(inorder(Solution().sufficientSubset(a, limit)))
