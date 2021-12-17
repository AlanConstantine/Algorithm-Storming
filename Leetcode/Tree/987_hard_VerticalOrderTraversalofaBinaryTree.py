# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-17 11:55:48

# 给你二叉树的根结点 root ，请你设计算法计算二叉树的 垂序遍历 序列。

# 对位于 (row, col) 的每个结点而言，其左右子结点分别位于 (row + 1, col - 1) 和 (row + 1, col + 1) 。树的根结点位于 (0, 0) 。

# 二叉树的 垂序遍历 从最左边的列开始直到最右边的列结束，按列索引每一列上的所有结点，形成一个按出现位置从上到下排序的有序列表。如果同行同列上有多个结点，则按结点的值从小到大进行排序。

# 返回二叉树的 垂序遍历 序列。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def verticalTraversal(self, root: TreeNode):
        if not root:
            return []
        co = {root: [0, 0]}
        s = [root]
        min_ = 0  # 从原点开始找最大值和最小值， 来记录二叉树的宽度
        max_ = 0
        while s:
            size = len(s)
            for _ in range(size):
                n = s.pop(0)
                co_ = co[n]
                if n.left:
                    s.append(n.left)
                    co[n.left] = [co_[0]+1, co_[1]-1]
                    min_ = min(min_, co[n.left][1])
                    max_ = max(max_, co[n.left][1])
                if n.right:
                    s.append(n.right)
                    co[n.right] = [co_[0]+1, co_[1]+1]
                    min_ = min(min_, co[n.right][1])
                    max_ = max(max_, co[n.right][1])
        ans = [[] for i in range(max_-min_+1)]  # 计算树的宽度，构建存储的数组
        co = sorted(co.items(), key=lambda item: (
            item[1][0], item[0].val))  # 排序结果，根据row大小和树的val排序
        zeroindex = 0-min_  # 找出原点
        for n, co_ in co:  # 循环加入结果
            col = co_[1]
            save_ = ans[col+zeroindex]
            save_.append(n.val)
            ans[col+zeroindex] = save_
        return ans


class Solution2:  # bfs， 但是不节约空间，需要额外的s栈来存储并访问
    def verticalTraversal(self, root: TreeNode):
        if not root:
            return []
        co = {root: [0, 0]}  # 用字典存储坐标
        s = [root]
        while s:
            size = len(s)
            for _ in range(size):
                n = s.pop(0)
                co_ = co[n]
                if n.left:
                    s.append(n.left)
                    co[n.left] = [co_[0]+1, co_[1]-1]
                if n.right:
                    s.append(n.right)
                    co[n.right] = [co_[0]+1, co_[1]+1]
        ans = []
        co = sorted(co.items(), key=lambda item: (
            item[1][1], item[1][0], item[0].val))  # 排序结果，依次根据col的大小、row大小和树的val排序
        current_col = None  # 判断插入的列是否和上一个一样
        for n, co_ in co:  # 循环加入有序的结果，因为已经拍过顺序，所以存储结果的时候就是有序存储的，不需要和方法1一样去定位
            if co_[1] != current_col:  # 插入的列和上一个不一样，说明上一列完成存储，进入下一列的存储
                current_col = co_[1]
                ans.append([])  # 创造新的容器来存新的一列
            ans[-1].append(n.val)
        return ans


class Solution:  # dfs，递归遍历，不需要额外的空间即栈存储并访问结点
    def verticalTraversal(self, root: TreeNode):
        if not root:
            return []
        co = {}

        def dfs(root, row, col):
            if not root:
                return None
            co[root] = [row, col]
            dfs(root.left, row+1, col-1)
            dfs(root.right, row+1, col+1)

        dfs(root, 0, 0)
        ans = []
        co = sorted(co.items(), key=lambda x: (
            x[1][1], x[1][0], x[0].val))
        currentcol = None
        for n, co_ in co:
            if co_[1] != currentcol:
                currentcol = co_[1]
                ans.append([])
            ans[-1].append(n.val)
        return ans


# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
# d = TreeNode(4)
# e = TreeNode(5)
# f = TreeNode(6)

# a.left = b
# a.right = c
# b.left = d
# b.right = f
# c.left = e


a = TreeNode(0)
b = TreeNode(1)
a.right = b

print(Solution().verticalTraversal(a))
