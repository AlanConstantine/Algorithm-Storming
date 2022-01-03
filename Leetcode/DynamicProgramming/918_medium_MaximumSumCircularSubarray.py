# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-03 15:17:22

# 给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。

# 在此处，环形数组意味着数组的末端将会与开头相连呈环状。（形式上，当0 <= i < A.length 时 C[i] = A[i]，且当 i >= 0 时 C[i+A.length] = C[i]）

# 此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。（形式上，对于子数组 C[i], C[i+1], ..., C[j]，不存在 i <= k1, k2 <= j 其中 k1 % A.length = k2 % A.length）

#  

# 示例 1：

# 输入：[1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3
# 示例 2：

# 输入：[5,-3,5]
# 输出：10
# 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
# 示例 3：

# 输入：[3,-1,2,-1]
# 输出：4
# 解释：从子数组 [2,-1,3] 得到最大和 2 + (-1) + 3 = 4
# 示例 4：

# 输入：[3,-2,2,-3]
# 输出：3
# 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-sum-circular-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution1:
    # 动态+暴力，循环数组的每个下标依次当第一个下标
    def maxSubarraySumCircular(self, nums) -> int:
        def help(nums):
            # 与53非循环数组解法相同
            size = len(nums)
            if size == 1:
                return nums[0]
            pre = nums[0]
            maxv = nums[0]
            for i in range(1, size):
                curr = max(nums[i], pre+nums[i])
                maxv = max(curr, maxv)
                pre = curr
            return maxv

        maxv_ = float("-inf")
        size = len(nums)
        while size >= 1:
            maxv_ = max(maxv_, help(nums))
            print(nums, maxv_)
            head = nums.pop(0)
            nums.append(head)
            size -= 1
        return maxv_


class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        # 最大的环形子数组和 = max(最大子数组和（非环形子数组），数组总和-最小子数组和（环形子数组）)
        # 证明：https://leetcode-cn.com/problems/maximum-sum-circular-subarray/solution/wo-hua-yi-bian-jiu-kan-dong-de-ti-jie-ni-892u/
        totalsum = 0
        maxsum = nums[0]
        minsum = nums[0]
        premax = 0  # 上一个元素的最大连续和
        premin = 0  # 上一个元素的最小连续和
        for a in nums:
            premax = max(premax+a, a)
            maxsum = max(premax, maxsum)
            premin = min(premin+a, a)
            minsum = min(premin, minsum)
            totalsum += a
        # 返回结果考虑三种情况：
        # 1. 数组中所有元素都小于0，则数组和只能是maxsum
        # 2. 考虑这个子数组不是环状的，就是说首尾不相连的结果，即53常规解法
        # 3. 考虑这个子数组一部分在首部，一部分在尾部，
        return max(maxsum, totalsum-minsum) if maxsum > 0 else maxsum


nums = [9, 3, 7, -6, 2, -1, 10, 8]
# nums = [1, -2, 3, -2]
# nums = [5, -3, 5]
print(Solution().maxSubarraySumCircular(nums))
