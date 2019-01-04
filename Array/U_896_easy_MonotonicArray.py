# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2018-10-25 17:17:28


# 如果数组是单调递增或单调递减的，那么它是单调的。

# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i] > = A[j]，那么数组 A 是单调递减的。

# 当给定的数组 A 是单调数组时返回 true，否则返回 false。


# 示例 1：

# 输入：[1, 2, 2, 3]
# 输出：true
# 示例 2：

# 输入：[6, 5, 4, 4]
# 输出：true
# 示例 3：

# 输入：[1, 3, 2]
# 输出：false
# 示例 4：

# 输入：[1, 2, 4, 5]
# 输出：true
# 示例 5：

# 输入：[1, 1, 1]
# 输出：true


# 提示：

# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag = set()
        A = sorted(list(set(A)))
        for i in range(len(A)):
            if i+1 == len(A):
                break
            if A[i] < A[i+1]:
                flag.add(1)
            elif A[i] > A[i+1]:
                flag.add(0)
        return True if len(flag) == 0 else False


A = [1, 2, 2, 3]

s = Solution()
print(s.isMonotonic(A))
