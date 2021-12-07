# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-07 12:40:44

# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

# 示例 1:

# 输入: [3,2,3,null,3,null,1]

#      3
#     / \
#    2   3
#     \   \
#      3   1

# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
# 示例 2:

# 输入: [3,4,5,1,3,null,1]

#      3
#     / \
#    4   5
#   / \   \
#  1   3   1

# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 方法1
# 由于不可以相邻打劫，因此只有两种情况可以打劫：
# 1：爷爷（当前节点）节点和四个孙子节点
# 2: 当前节点的两个孩子节点
# 对比两个结果返回最大值即可


class Solution1:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        money = root.val  # 爷爷（当前节点值）的钱
        if root.left:
            money += self.rob(root.left.left) + \
                self.rob(root.left.right)  # 左孙子节点的钱
        if root.right:
            money += self.rob(root.right.left) + \
                self.rob(root.right.right)  # 有孙子节点的钱
        return max(money, self.rob(root.left)+self.rob(root.right))  # 对比两种情况的大小

# 方法2
# 方法1当遍历到爷爷节点的时候，实际上也计算了孩子节点和孙子节点的结果
# 再继续向孩子节点即孩子节点变成爷爷节点的时候，实际上其孩子节点又会被重复计算，所以时间复杂变大，出现重复子问题
# 因此可以使用动态规划：
# 对比斐波那契数列用数组存储计算结果，由于二叉树不适合拿数组当缓存，我们这次使用哈希表来存储结果，TreeNode 当做 key，能偷的钱当做 value


class Solution2:
    s = {}  # 用字典来记录被访问过的节点的结果

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root in self.s:
            return self.s[root]  # 查询当前节点是否被计算过，是则取出计算的结果

        money = root.val
        if root.left:
            money += self.rob(root.left.left) + \
                self.rob(root.left.right)  # 左孙子节点的钱
        if root.right:
            money += self.rob(root.right.left) + \
                self.rob(root.right.right)  # 有孙子节点的钱
        res = max(money, self.rob(root.left)+self.rob(root.right))  # 对比两种情况的大小
        self.s[root] = res  # 存储当前节点的结果
        return res

# 方法3
# 用长度为2的数组来表示当前节点的状态
# 0位置表示当前节点不偷的时候获得的收益
# 1位置表示当前节点偷的时候获得的收益


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        def help(root):
            if not root:
                return [0, 0]
            leftres = help(root.left)
            rightres = help(root.right)
            # 初始化当前节点的结果
            res = [0, 0]
            # 当前节点不偷的话，则要考虑两个孩子节点是否被偷的结果，因为当前节点不偷，不代表孩子节点一定会被偷，需要综合考虑孩子节点他们自己的不偷和偷的状态
            res[0] = max(leftres[0], leftres[1]) + \
                max(rightres[0], rightres[1])
            # 当前节点偷的话, 则返回孩子节点不偷的结果加上当前节点被偷的结果
            res[1] = leftres[0] + rightres[0] + root.val
            return res
        res = help(root)
        return max(res[0], res[1])
