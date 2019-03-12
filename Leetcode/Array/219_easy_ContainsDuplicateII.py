# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使 nums [i] = nums [j]，并且 i 和 j 的绝对差值最大为 k。


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cdict = {}
        for i, e in enumerate(nums):
            if e in cdict and i - cdict[e] <= k:
                return True
            cdict[e] = i
        return False


k = 2
nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 2, 3]
print(Solution().containsNearbyDuplicate(nums2, k))
