# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-15 16:35:00

# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 说明：

# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

# 示例 1:

# 输入: [2,2,1]
# 输出: 1
# 示例 2:

# 输入: [4,1,2,1,2]
# 输出: 4


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a


nums = [4, 1, 2, 1, 2]
s = Solution()
print(s.singleNumber(nums))


# 异或知识
# 异或的特性：
# 1.恒定律：A ^ 0 = A
# 2.归零率：A ^ A = 0
# 3.交换律：A ^ B = B ^ A
# 4.结合律：(A ^ B) ^ C = A ^ (B ^ C)

# 假设所有的数组为：abcbcda
# a ^ b ^ c ^ b ^ c ^ d ^ a
# = a ^ a ^ b ^ b ^ c ^ c ^ d
# = 0 ^ 0 ^ 0 ^ d
# = d
