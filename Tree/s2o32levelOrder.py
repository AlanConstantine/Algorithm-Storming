# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-26 13:41:35


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        s = [root]
        ans = [[root.val]]

        while s:
            stmp = []
            anstmp = []
            for n in s:
                if n.left:
                    stmp.append(n.left)
                    anstmp.append(n.left.val)
                if n.right:
                    stmp.append(n.right)
                    anstmp.append(n.right.val)
            if anstmp:
                ans.append(anstmp)
            s = stmp
        return ans
