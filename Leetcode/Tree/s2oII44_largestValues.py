# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        s = [root]
        while s:
            ans.append(max([n.val for n in s]))  # 不一定用遍历，可以用一个最小值来比较
            stmp = []
            for n in s:
                if n.left:
                    stmp.append(n.left)
                if n.right:
                    stmp.append(n.right)
            s = stmp
        return ans
