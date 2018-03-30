# 给定一个序列（至少含有 1 个数），从该序列中寻找一个连续的子序列，使得子序列的和最大。
# 例如，给定序列 [-2,1,-3,4,-1,2,1,-5,4]，
# 连续子序列 [4,-1,2,1] 的和最大，为 6。


class Solution1:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = min(nums)
        left = 0
        if len(nums) == 1:
            return nums[0]
        while left <= len(nums) - 1:
            for right in range(len(nums), 0, -1):
                if right <= left:
                    break
                splitsum = sum(nums[left:right])
                if splitsum > max:
                    max = splitsum
            left += 1
        return max


class Solution2:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum, _sum = 0, 0
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum > maxsum:
                maxsum = _sum
            elif _sum < 0:
                _sum = nums[i]
        return maxsum


nums = [-2, -1]
print(Solution2().maxSubArray(nums))
