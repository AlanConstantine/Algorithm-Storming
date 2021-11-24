# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-24 10:08:59

# 给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。

# 对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

# 返回这些数字之和。题目数据保证答案是一个 32 位 整数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        pass
