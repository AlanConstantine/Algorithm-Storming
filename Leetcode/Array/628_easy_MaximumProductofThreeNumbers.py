# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'Array'))
    print(os.getcwd())
except:
    pass

# %%
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

# 示例 1:

# 输入: [1,2,3]
# 输出: 6
# 示例 2:

# 输入: [1,2,3,4]
# 输出: 24


# %%
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0] < 0 and nums[-1] > 0:
            return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
        else:
            return nums[-1]*nums[-2]*nums[-3]


# %%
s = Solution()
nums = [1, 2, 3, 4]
print(s.maximumProduct(nums))
