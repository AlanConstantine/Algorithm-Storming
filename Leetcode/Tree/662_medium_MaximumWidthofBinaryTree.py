# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-23 15:33:04

# 给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。

# 每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。

# 示例 1:

# 输入:

#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9

# 输出: 4
# 解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
# 示例 2:

# 输入:

#           1
#          /
#         3
#        / \
#       5   3

# 输出: 2
# 解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-width-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 利用完全二叉树的性质，利用BFS遍历重新给节点编码
# 编码后每层的宽度就是最右节点值-最左节点值+1
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        root.val = 1
        s = [root]
        maxwidth = 0
        while s:
            size = len(s)
            width = s[-1].val - s[0].val+1
            for _ in range(size):
                n = s.pop(0)
                if n.left:
                    s.append(n.left)
                    n.left.val = 2*n.val+1  # 左节点的值为父节点的值*2+1
                if n.right:
                    s.append(n.right)
                    n.right.val = 2*n.val+2  # 左节点的值为父节点的值*2+2
            maxwidth = max(maxwidth, width)
        return maxwidth


a = TreeNode(1)
b = TreeNode(3)
c = TreeNode(2)
d = TreeNode(5)
e = TreeNode(6)
f = TreeNode(9)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
d.left = e
c.right = f
f.right = g

print(Solution().widthOfBinaryTree(a))
