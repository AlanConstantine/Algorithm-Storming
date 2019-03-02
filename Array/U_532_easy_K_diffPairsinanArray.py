# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2018-04-26 22:29:03
# 给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.

# 示例 1:

# 输入: [3, 1, 4, 1, 5], k = 2
# 输出: 2
# 解释: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
# 尽管数组中有两个1，但我们只应返回不同的数对的数量。
# 示例 2:

# 输入:[1, 2, 3, 4, 5], k = 1
# 输出: 4
# 解释: 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
# 示例 3:

# 输入: [1, 3, 1, 5, 4], k = 0
# 输出: 1
# 解释: 数组中只有一个 0-diff 数对，(1, 1)。
# 注意:


# 数对 (i, j) 和数对 (j, i) 被算作同一数对。
# 数组的长度不超过10,000。
# 所有输入的整数的范围在 [-1e7, 1e7]。
class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        counter = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k and [nums[i], nums[j]] not in counter:
                    counter.append([nums[i], nums[j]])
        return len(counter)


# class Solution:
#     def findPairs(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         temp = {}
#         for i in nums:
#             if i in temp:
#                 i++
#             else:
#                 temp[i] = 1
#         pass

        # temp = list(set(nums))
        # if k == 0 and len(temp) != 1:
        #     return len(nums)-len(temp)
        # if k < 0:
        #     return 0
        # count = 0
        # for i in range(len(temp)):
        #     if temp[i]+k in temp or temp[i]-k in temp[i+1:]:
        #         count += 1
        # return count


k = 0
nums = [1, 1, 1, 1, 1]
num = Solution().findPairs(nums, k)
print(num)
