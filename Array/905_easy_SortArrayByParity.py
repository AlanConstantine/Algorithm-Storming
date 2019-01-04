# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2018-10-25 14:17:20

# 给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。

# 你可以返回满足此条件的任何数组作为答案。


# 示例：

# 输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        out = []
        for i in range(len(A)):
            if A[i] == 0 or A[i] % 2 == 0:
                out.insert(0, A[i])
            else:
                out.append(A[i])
        return out


class Solution2:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A.insert(0, A[i])
                del A[i+1]
        return out


A = [3, 1, 2, 4]
s = Solution2()
print(s.sortArrayByParity(A))
