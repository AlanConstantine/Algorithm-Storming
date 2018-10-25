# 给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。

# 例如， 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ret = []
        for i in range(len(nums)):
            if nums[i] != 0:
                ret.append(nums[i])
        get_zero = (len(nums)-len(ret))*[0]
        nums = ret
        nums.extend(get_zero)
        return nums


class Solution2:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
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


class Solution3:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        self.trs(0, nums)

    def trs(self, begin, nums):
        for i in range(begin, len(nums)):
            if nums[i] == 0 and i + 1 != len(nums):
                if nums[i + 1] == 0:
                    self.trs(i + 1, nums)
                temp = nums[i + 1]
                nums[i + 1] = nums[i]
                nums[i] = temp
            print(nums)


# class Solution3:
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         print(nums)
#         if len(nums) == 0:
#             return
#         j = len(nums) - 1
#         for i in range(len(nums) - 1, 1, -1):
#             for l in range(i, j + 1):
#                 if l + 1 == len(nums):
#                     break
#                 temp = nums[l]
#                 nums[l] = nums[l + 1]
#                 nums[l + 1] = temp
#             j = j - 1
#         print(nums)


nums = [0, 1, 0, 3, 12]
# nums = [0, 0, 1]
print(Solution().moveZeroes(nums))
