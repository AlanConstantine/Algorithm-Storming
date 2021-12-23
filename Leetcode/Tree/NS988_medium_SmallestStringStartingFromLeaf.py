# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-23 15:23:07

# 给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个从 0 到 25 的值，分别代表字母 'a' 到 'z'：值 0 代表 'a'，值 1 代表 'b'，依此类推。

# 找出按字典序最小的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。

# （小贴士：字符串中任何较短的前缀在字典序上都是较小的：例如，在字典序上 "ab" 比 "aba" 要小。叶结点是指没有子结点的结点。）

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/smallest-string-starting-from-leaf
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root) -> str:
        if not root:
            return ""
        res = ""

        def dfs(root):
            pass
