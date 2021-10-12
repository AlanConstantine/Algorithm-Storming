# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-10-12


# https://mp.weixin.qq.com/s?__biz=MzI2NjA3NTc4Ng==&mid=2652090803&idx=2&sn=1e6114df12d31fdd59bce411ac109890&chksm=f174ba56c6033340f2f7808c5379cc69321d7ba4a488205812fc0088e60bdc6bc2eccd8b3c64&sessionid=1634002284&subscene=93&scene=90&clicktime=1634002440&ascene=56&devicetype=iOS15.0.1&version=18000e2b&nettype=3G+&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&fontScale=100&exportkey=AUJvWXIUtoBFk%2FbbthukKaQ%3D&pass_ticket=nY09OdWURWKSWKcHKzjKQyIxwaAz95cLu%2Bhq7WO5eNTuKaw8UEXhRTwpQE3znRcL&wx_header=1
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

# 示例 1:

# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
# 示例 2:

# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
# 说明:

# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pre_traversal(node):
    # root, left, right
    res = []
    if node:
        res.append(node.val)
        res = res + pre_traversal(node.left)
        res = res + pre_traversal(node.right)
    return res


def in_traversal(node):
    # left, root, right
    res = []
    if node:
        res = in_traversal(node.left)
        res.append(node.val)
        res = res + in_traversal(node.right)
    return res


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        pass


a = TreeNode(6)
b = TreeNode(2)
c = TreeNode(8)
d = TreeNode(0)
e = TreeNode(4)
f = TreeNode(7)
g = TreeNode(9)
h = TreeNode(3)
i = TreeNode(5)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = h
e.right = i
c.left = f
c.right = g

print(in_traversal(a))
