# 满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。

# 返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。

# 答案中每个树的每个结点都必须有 node.val=0。

# 你可以按任何顺序返回树的最终列表。


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n):
        res = []
        if n % 2 == 0:  # 0 % 2也等于0
            return res
        if n == 1:
            return [TreeNode(0)]
        for i in range(1, n, 2):
            # 遍历每一个数字轮流当根节点
            # 递归思路，不需要关心发生了什么，只关系把n分解成两个子问题传递给下一个任务即可
            lefts = self.allPossibleFBT(i)  # 给i数字个给左子树
            # 剩下n-i-1则为右子树的, -1是因为有一个是要用来作为根节点的
            rights = self.allPossibleFBT(n-i-1)
            # 遍历子问题中产生的所有左右子树
            for l in lefts:
                for r in rights:
                    root = TreeNode(0, l, r)  # 加入到根节点
                    res.append(root)
        return res


class Solution2:
    def allPossibleFBT(self, n: int):
        dp = [[] for _ in range(n + 1)]
        dp[1].append(TreeNode(0))
        for i in range(3, n + 1, 2):  # 遍历所有节点数量
            for j in range(1, i - 1, 2):  # 遍历左子树所有节点数量，从1到i-2
                lefts, rights = dp[j], dp[i - j - 1]
                for left in lefts:
                    for right in rights:
                        dp[i].append(TreeNode(0, left, right))
        return dp[n]
