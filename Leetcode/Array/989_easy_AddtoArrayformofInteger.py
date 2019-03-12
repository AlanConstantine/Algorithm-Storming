# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-02-20 15:48:51

# 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。

# 给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。


# 示例 1：

# 输入：A = [1,2,0,0], K = 34
# 输出：[1,2,3,4]
# 解释：1200 + 34 = 1234
# 解释 2：

# 输入：A = [2,7,4], K = 181
# 输出：[4,5,5]
# 解释：274 + 181 = 455
# 示例 3：

# 输入：A = [2,1,5], K = 806
# 输出：[1,0,2,1]
# 解释：215 + 806 = 1021
# 示例 4：

# 输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
# 输出：[1,0,0,0,0,0,0,0,0,0,0]
# 解释：9999999999 + 1 = 10000000000

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        # if K == 0:
        #     return A
        # K = str(K)
        # m = 0
        # res = []
        # for i in range(len(A)):
        #     p = -1*(i+1)
        #     plusnum = A[p]
        #     if m == 1:
        #         plusnum = plusnum+m
        #         m = 0
        #     if i >= len(K):
        #         if plusnum >= 10:
        #             res.insert(0, plusnum-10)
        #             m += 1
        #         else:
        #             res.insert(0, plusnum)
        #     if i < len(K):
        #         sum_ = plusnum+int(K[p])
        #         if sum_ >= 10:
        #             m += 1
        #             sum_ -= 10
        #         res.insert(0, sum_)
        # if m == 1:
        #     res.insert(0, 1)
        # return res


class SolutionII(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        return list(map(lambda y: int(y), list(str(int(''.join(map(lambda x: str(x), A)))+K))))


def main():
    K = 806
    A = [2, 1, 5]
    s = Solution()
    print(s.addToArrayForm(A, K))


if __name__ == "__main__":
    main()
