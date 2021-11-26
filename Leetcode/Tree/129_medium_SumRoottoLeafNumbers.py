# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-26 13:47:47

# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
# 每条从根节点到叶节点的路径都代表一个数字：

# 例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
# 计算从根节点到叶节点生成的 所有数字之和 。

# 叶节点 是指没有子节点的节点。

#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.ans = []
        self.s = []

        def dfs(root):
            if not root:
                return
            self.s.append(str(root.val))
            if not root.left and not root.right:
                self.ans.append(int(''.join(self.s)))
                self.s.pop()
                return
            dfs(root.left)
            dfs(root.right)
            self.s.pop()
            return
        dfs(root)
        return sum(self.ans)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, sum):
            if not root:
                return 0
            if not root.left and not root.right:
                return sum*10 + root.val  # 若子树为空，则返回当前计算
            # 否则把当前计算传到下一层
            return dfs(root.left, sum*10+root.val) + dfs(root.right, sum*10+root.val)
        return dfs(root, 0)


a = TreeNode(4)
b = TreeNode(9)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(0)

a.left = b
b.left = c
b.right = d
a.right = e

print(Solution().sumNumbers(a))
