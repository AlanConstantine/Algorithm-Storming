# 给定一个数组和一个值，在这个数组中原地移除指定值和返回移除后新的数组长度。
# 不要为其他数组分配额外空间，你必须使用 O(1) 的额外内存原地修改这个输入数组。
# 元素的顺序可以改变。超过返回的新的数组长度以外的数据无论是什么都没关系。


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[i]
                nums[i] = nums[pointer]
                nums[pointer] = temp
                pointer += 1
        print(nums)
        return pointer


nums = [3, 2, 2, 3]
val = 4
print(Solution().removeElement(nums, val))
