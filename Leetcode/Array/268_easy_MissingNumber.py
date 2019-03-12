# 给出一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, e in enumerate(sorted(nums)):
            if i != e:
                return i
        return sorted(nums)[-1] + 1


class Solution2:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return int(n * (n + 1) / 2) - sum(nums)


nums = [1, 0]
print(Solution().missingNumber(nums))
