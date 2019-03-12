# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-02-26 11:28:37

# 给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

# 让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

# A.length >= 3
# 在 0 < i < A.length - 1 条件下，存在 i 使得：
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[B.length - 1]


# 示例 1：

# 输入：[2,1]
# 输出：false
# 示例 2：

# 输入：[3,5,5]
# 输出：false
# 示例 3：

# 输入：[0,3,2,1]
# 输出：true


# 提示：

# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3 or A[0] >= A[1]:
            return False
        s = 0
        e = len(A)-1
        while s < len(A)-1 and A[s+1] > A[s]:
            s += 1
        while e > 0 and A[e-1] > A[e]:
            e -= 1
        return 0 < e == s < len(A)-1


s = Solution()
A = [0, 3, 2, 1]
print(s.validMountainArray(A))
