# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-09 10:05:22

# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

#  

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：

# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
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
        ans.append([root.val])
        d = 1
        while s:
            size = len(s)
            stmp = []
            d += 1
            for _ in range(size):
                n = s.pop(0)
                if n.left:
                    s.append(n.left)
                    stmp.append(n.left.val)
                if n.right:
                    s.append(n.right)
                    stmp.append(n.right.val)
            if stmp:
                if d % 2 == 0:
                    stmp = stmp[::-1]
                ans.append(stmp)
        return ans
