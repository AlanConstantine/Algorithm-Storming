# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-23 13:42:19

# 检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。

# 如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

# 注意：此题相对书上原题略有改动。

# 示例1:

#     输入：t1 = [1, 2, 3], t2 = [2]
#     输出：true
# 示例2:

#     输入：t1 = [1, null, 2, 4], t2 = [3, 2]
#     输出：false
# 提示：

# 树的节点数目范围为[0, 20000]。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/check-subtree-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
from _typeshed import Self


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def dfs(root):
            res = '#'
            if not root:
                return res
            res += str(root.val)
            res += dfs(root.left)
            res += dfs(root.right)
            return res

        t1s = dfs(t1)
        t2s = dfs(t2)
        return t2s in t1s


class Solution2:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1:
            return not t2
        return self.isequal(t1, t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)

    def isequal(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and self.isequal(t1.left, t2.left) and self.isequal(t1.right, t2.right)


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True

        if not t1 and t2:
            return False

        if not t2:
            return True

        if t1.val == t2.val:
            if self.checkSubTree(t1.left, t2.left) and self.checkSubTree(t1.right, t2.right):
                return True

        return self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

d = TreeNode(2)

a.left = b
a.right = c
print(Solution().checkSubTree(a, d))
