# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-02 13:27:05

# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

#  

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回：

# [3,9,20,15,7]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        ans = []
        if not root:
            return ans
        s = [root]
        ans.append(root.val)
        while s:
            n = s.pop(0)
            if n.left:
                s.append(n.left)
                ans.append(n.left.val)
            if n.right:
                s.append(n.right)
                ans.append(n.right.val)
        return ans
