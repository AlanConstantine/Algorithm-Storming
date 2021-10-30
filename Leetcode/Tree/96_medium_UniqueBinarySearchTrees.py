# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#  注意：n=0的时候也就是空树也算一棵树，
# 设： G[n] 表示输入一个整数n，可以产生的BST总数, f[i]表示根节点为i时的BST总数
# 当以i为根节点的时候，左子树的根节点为[1, 2, ..., i-1]共i-1-1+1=i-1个节点,而i-1个节点又可以继续产生G[i-1]棵树
# 右子树的根节点为[i+1, i+2, ..., n]共n-(i+1)-1=n-i个节点，n-i个节点可以产生G[n-i]
# 则f[i]根节点为i时的BST总数=G[i-1]*G[n-i]： f[i]=G[i-1]*G[n-i]
# 而G[n] = f[1] + f[2] + ... + f[n]

class Solution:
    def numTrees(self, n):
        if n == 0:
            G = [1]
        elif n == 1:
            G = [1, 1]
        else:
            G = [1, 1] + [0] * (n-2+1)
            for i in range(2, n+1):
                for j in range(1, i+1):
                    G[i] += G[j-1]*G[i-j]
        return G[n]


S = Solution()
print(S.numTrees(2))
