# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-22 20:18:02

# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    res = 0

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        self.dfs(root, targetSum)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.res

    def dfs(self, root, tar):
        if not root:
            return
        tar -= root.val
        if tar == 0:
            self.res += 1
        self.dfs(root.left, tar)
        self.dfs(root.right, tar)

# Reference: https://leetcode-cn.com/problems/path-sum-iii/solution/dui-qian-zhui-he-jie-fa-de-yi-dian-jie-s-dey6/
# 前缀和：节点的前缀和=根节点到当前节点的路径上所有节点的和
# 利用先序遍历二叉树，记录下根节点 root 到当前节点 p的路径上除当前节点以外所有节点的前缀和

# 如果targetSum == A节点的前缀和 - B节点的前缀和， 且A一定是B节点的子树中的节点，则B到A的路径满足要求


class Solution:

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        # 定义hashmap来存储前缀和，key为前缀和，value为前缀和的数量
        self.prefix = collections.defaultdict(int)
        self.prefix[0] = 1  # 用叶子结点初始化，即前缀树为0的个数至少是一个（叶子结点）

        def dfs(root, curr):
            # curr用于累加记录前缀和
            if not root:
                return 0
            curr += root.val  # 计算当前节点的前缀和
            res = self.prefix[curr-targetSum]  # 获取满足要求的前缀和的个数
            # 计数计算所得的前缀和(特殊情况：curr--targetSum也可能等于curr)，所以65行代码一定在66行前面
            self.prefix[curr] += 1
            res += dfs(root.left, curr)  # 加上左子树的结果
            res += dfs(root.right, curr)  # 加上右子树的结果
            self.prefix[curr] -= 1  # 状态回归，因为只能服务于当前节点的子节点
            return res  # 返回所有结果

        return dfs(root, 0)
