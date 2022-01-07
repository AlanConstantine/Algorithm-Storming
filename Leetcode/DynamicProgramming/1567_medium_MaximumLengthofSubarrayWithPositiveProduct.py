# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-05 16:47:25

# 给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。

# 一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。

# 请你返回乘积为正数的最长子数组长度。

# 示例  1：

# 输入：nums = [1,-2,-3,4]
# 输出：4
# 解释：数组本身乘积就是正数，值为 24 。
# 示例 2：

# 输入：nums = [0,1,-2,-3,-4]
# 输出：3
# 解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
# 注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
# 示例 3：

# 输入：nums = [-1,-2,-3,0,1]
# 输出：2
# 解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
# 示例 4：

# 输入：nums = [-1,2]
# 输出：1
# 示例 5：

# 输入：nums = [1,2,3,5,-6,4,0,10]
# 输出：4


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    # dp
    def getMaxLen(self, nums) -> int:
        size = len(nums)
        pos = [0] * size
        neg = [0] * size  # 利用pos和neg来存储每一个下标前的最长连续最大和最小的乘积子数组
        if nums[0] > 0:
            pos[0] = 1
        if nums[0] < 0:
            neg[0] = 1
        res = pos[0]
        for i in range(1, size):
            if nums[i] > 0:  # 若当前下标对应的元素是正数, 当前位为正数，乘上一位对应的最大乘积为仍然是正数，因此当前位正数最大子数组长度位
                pos[i] = pos[i-1] + 1  # 连续正数+1
                # 如果neg[i-1]>0，说明i-1的负数最小乘积乘于当前的正数会仍然为负数，而且最小
                neg[i] = neg[i-1] + 1 if neg[i-1] > 0 else 0
            elif nums[i] < 0:
                # 当前元素为负数的时候，正数最大乘积的就是负数最小乘积连续长度+1，而负数则为正数最大乘积连续长度+1，即pos[i]和neg[i]的结果要发生交换
                # 且neg[i-1]需要！=0，因为只有不为0当前的下标才能取到最大乘积值
                pos[i] = neg[i-1] + 1 if neg[i-1] > 0 else 0
                neg[i] = pos[i-1] + 1
            else:
                pos[i] = neg[i] = 0
                # 当前需要进行乘的值如果等于0则正负最长子数组长度均需重新置零重新从下一个数进行遍历
            res = max(res, pos[i])  # 每次都比较取最大的结果
        return res


class Solution2:
    # 根据dp优化空间
    def getMaxLen(self, nums) -> int:
        prepos = 0
        preneg = 0
        res = 0
        for i in range(len(nums)):
            currpos = 0
            currneg = 0
            if nums[i] == 0:
                currpos = 0
                currneg = 0
                prepos, preneg = currpos, currneg
            elif nums[i] > 0:
                currpos = prepos + 1
                currneg = preneg + 1 if preneg != 0 else 0
                prepos, preneg = currpos, currneg
            elif nums[i] < 0:
                currneg = prepos + 1
                currpos = preneg + 1 if preneg != 0 else 0
                prepos, preneg = currpos, currneg
            res = max(res, currpos)
        return res


class Solution:
    # 二次根据dp优化空间
    def getMaxLen(self, nums) -> int:
        prepos, preneg = 0, 0
        res = 0
        for n in nums:
            if n == 0:
                prepos, preneg = 0, 0
            elif n > 0:
                prepos, preneg = prepos + 1, preneg + 1 if preneg != 0 else 0
            else:
                preneg, prepos = prepos + 1, preneg + 1 if preneg != 0 else 0
            res = max(res, prepos)
        return res


nums = [-1, -2, -3, 0, 1]
nums = [0, 1, -2, -3, -4]
print(Solution().getMaxLen(nums))
