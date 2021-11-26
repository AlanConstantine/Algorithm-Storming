# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-26 13:31:02

# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

#  

# 示例 1：

# 输入：
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出：[3, 14.5, 11]
# 解释：
# 第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []
        ans = [root.val]
        s = [root]
        while s:
            stmp = []
            anstmp = 0
            for n in s:
                if n.left:
                    stmp.append(n.left)
                    anstmp += n.left.val
                if n.right:
                    stmp.append(n.right)
                    anstmp += n.right.val
            if not stmp:
                break
            ans.append(anstmp/len(stmp))
            s = stmp
        return ans
