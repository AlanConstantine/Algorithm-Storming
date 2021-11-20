# 给定一棵二叉搜索树，请找出其中第k大的节点。

#  

# 示例 1:

# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4
# 示例 2:

# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # res = None
    # k = None

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k

        if not root:
            return

        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)
        dfs(root)
        return self.res


#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4
a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(2)
e = TreeNode(4)

a.left = b
a.right = e
b.right = c

print(Solution().kthLargest(a, 3))
