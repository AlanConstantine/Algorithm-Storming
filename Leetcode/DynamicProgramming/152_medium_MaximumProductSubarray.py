# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-05 16:03:11

# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

#  

# 示例 1:

# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:

# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-product-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    # 类似53题，但是需要考虑负负得正的情况，所以在找最大值的同时也要找最小值，因为最小值可能为负数且再乘上一个负数就为正数且有机会成且最大值
    def maxProduct(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        premax = 0
        premin = 0
        maxv = nums[0]
        minv = nums[0]
        for n in nums:
            # 对于当前的下标最大的解，对比的时候要考虑上一个最小值乘上当前下标的情况
            curr = max(premax*n, n, premin*n)
            currmin = min(premin*n, n, premax*n)  # 对于当前的小标最小解，与找最大值相似
            maxv = max(maxv, curr)
            premax = curr
            minv = min(minv, currmin)
            premin = currmin
        return maxv


class Solution:
    # 优化空间（其实没差）
    def maxProduct(self, nums) -> int:
        maxF = nums[0]
        minF = nums[0]
        ans = nums[0]
        for n in nums[1:]:
            maxv, minv = maxF, minF
            maxF = max(maxv*n, n, minv*n)
            minF = min(minv*n, n, maxv*n)
            ans = max(maxF, ans)
        return ans


nums = [2, 3, -2, 4]
# nums = [-2, 0, -1]
# nums = [-2, -1, 3, 0]
# nums = [-2]
nums = [-4, -3, -2]

print(Solution().maxProduct(nums))
