# 给定一个整数数组，判断是否存在重复元素。

# 如果任何值在数组中出现至少两次，函数应该返回 true。如果每个元素都不相同，则返回 false。


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cdict = {}
        for i in nums:
            if i in cdict:
                return True
            else:
                cdict[i] = 1
        return False


class Solution2:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 2, 3]
print(Solution().containsDuplicate(nums2))
