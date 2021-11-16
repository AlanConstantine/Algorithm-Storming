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
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        pass
