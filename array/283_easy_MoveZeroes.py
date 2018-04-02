# 给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。

# 例如， 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.trs(nums)
        return nums

    def trs(self, nums):
        try:
            zp = nums.index(0)
            nums.remove(nums[zp])
            nums.append(0)
            self.trs(nums)
        except:
            return


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(nums))
