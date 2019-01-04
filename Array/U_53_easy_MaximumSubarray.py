# 给定一个序列（至少含有 1 个数），从该序列中寻找一个连续的子序列，使得子序列的和最大。
# 例如，给定序列 [-2,1,-3,4,-1,2,1,-5,4]，
# 连续子序列 [4,-1,2,1] 的和最大，为 6。

# 动态规划


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum, _sum = 0, 0
        for i in range(len(nums)):
            maxsum = nums[i]
            if _sum < 0:
                _sum = nums[i]
            else:
                _sum += nums[i]
            if _sum > maxsum:
                maxsum = _sum
        return maxsum


nums = [-2, -1, 1, 2]
print(Solution().maxSubArray(nums))
