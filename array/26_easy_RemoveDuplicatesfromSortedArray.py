class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != nums[pointer]:
                nums[pointer + 1] = nums[i]
                pointer += 1
        print(nums)
        return pointer + 1


nums = [1, 1, 1, 2, 2, 3]
print(Solution().removeDuplicates(nums))
