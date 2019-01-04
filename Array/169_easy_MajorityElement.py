# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且数组中的众数永远存在。


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        cdict = {}
        cmax = [0, None]
        for i in range(len(nums)):
            if nums[i] in cdict:
                c = cdict[nums[i]]
                cdict[nums[i]] = c + 1
                if c + 1 > cmax[0]:
                    cmax = [c + 1, nums[i]]
            else:
                cdict[nums[i]] = 1
        return cmax[1]


class Solution2:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]


nums = [1]
print(Solution().majorityElement(nums))
