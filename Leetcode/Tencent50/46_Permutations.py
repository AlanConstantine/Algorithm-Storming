# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-11 18:22:14

# 给定一个没有重复数字的序列，返回其所有可能的全排列。

# 示例:

# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        n = len(nums)

        for num in nums:
            new_res = []
            for i in range(len(res)):
                prev = res[i]
                prev.append(num)
                for j in range(len(prev)):
                    prev[j], prev[-1] = prev[-1], prev[j]
                    new_res.append(prev[:])
                    prev[j], prev[-1] = prev[-1], prev[j]
            res = new_res
        return res


class SolutionII(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(results, tmp, candidates):
            if len(tmp) == len(candidates):
                results.append(list(tmp))
            for c in candidates:
                if c not in tmp:
                    tmp.append(c)
                    dfs(results, tmp, candidates)
                    tmp.pop()
        results = []
        dfs(results, [], nums)
        return results


nums = [1, 2, 3]
s = Solution()
print(s.permute(nums))
