# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2018-10-25 17:17:28

# 如果数组是单调递增或单调递减的，那么它是单调的。

# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

# 当给定的数组 A 是单调数组时返回 true，否则返回 false。

#  

# 示例 1：

# 输入：[1,2,2,3]
# 输出：true
# 示例 2：

# 输入：[6,5,4,4]
# 输出：true
# 示例 3：

# 输入：[1,3,2]
# 输出：false
# 示例 4：

# 输入：[1,2,4,5]
# 输出：true
# 示例 5：

# 输入：[1,1,1]
# 输出：true
#  

# 提示：

# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
# 通过次数62,293提交次数106,671

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/monotonic-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution2:
    def isMonotonic(self, A):
        return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in range(len(A) - 1)))


class Solution:
    def isMonotonic(self, nums) -> bool:
        flag = set()
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                flag.add(1)
            if nums[i] < nums[i-1]:
                flag.add(0)
        return True if len(flag) <= 1 else False


A = [1, 2, 2, 3]

s = Solution()
print(s.isMonotonic(A))
