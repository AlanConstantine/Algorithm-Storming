# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'Array'))
    print(os.getcwd())
except:
    pass

# %%
# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。

# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

# 示例:

# 输入:
# [4,3,2,7,8,2,3,1]

# 输出:
# [5,6]


# %%
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])
        print(nums)
        print([i + 1 for i in range(len(nums)) if nums[i] > 0])


# %%
nums = [4, 3, 2, 7, 8, 2, 3, 1]
s = Solution()
s.findDisappearedNumbers(nums)
