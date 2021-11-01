# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。
# 可以按 任意顺序 返回答案。

# 思路，从1到n中轮流取一个数字i作为根节点，
# 那么子问题就是当i作为根节点的时候，[1, i-1]则为左边可作为根节点的数字集，[i+1, n]则为右边可作为根节点的数字集
# 同理重复第一步，依次划分解决问题。
# 设一个新的函数，用来处理[start, end]所产生的树
# 边界问题当n=0的时候返回[]。
# 用到了BST思路

class TreeNode(object):
    def __init__(self, val):
        super().__init__()
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        res = []
        if n == 0:
            return res
        else:
            return self.getTree(1, n)  # 设定遍历范围让[1, n]的数字轮流当根节点

    def getTree(self, start, end):
        res = []
        if start > end:  # 当上下限不一致的时候说明遍历完成
            res.append(None)  # 为什么返回None？ 因为start>end表示子树已经遍历完成，返回一个空树给上一个节点
            return res
        else:
            for i in range(start, end+1):  # 遍历给定范围内的数字来当根节点
                res_left = self.getTree(start, i-1)  # 返回左边，即小于i的所有产生的树的情况
                res_right = self.getTree(i+1, end)  # 返回右边，大于i小于等于n的所有产生的树的情况
                for left_t in res_left:  # 得到返回的左右树后，遍历返回的结果，进行排练组合
                    for right_t in res_right:
                        root = TreeNode(i)
                        root.left = left_t
                        root.right = right_t
                        res.append(root)
            return res


S = Solution()
S.generateTrees(3)
