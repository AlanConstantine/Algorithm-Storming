# 将包含 n 个元素的数组向右旋转 k 步。
# 例如，如果  n = 7 ,  k = 3，给定数组  [1,2,3,4,5,6,7]  ，向右旋转后的结果为 [5,6,7,1,2,3,4]。
# 注意:
# 尽可能找到更多的解决方案，这里最少有三种不同的方法解决这个问题。
# [显示提示]
# 提示:
# 要求空间复杂度为 O(1)


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-1)
        print(nums)
        self.reverse(nums, 0, k-1)
        print(nums)
        self.reverse(nums, k, n-1)

    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1


class SolutionII:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        for i in range(k):
            temp = nums[n-1]
            for j in range(n-1, 0, -1):
                nums[j] = nums[j-1]
            nums[0] = temp
        print(nums)


class SolutionIII:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[n-k:]+nums[:n-k]
        print(nums)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
SolutionIII().rotate(nums, k)
