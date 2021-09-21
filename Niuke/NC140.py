# NC140 排序
# link: https://www.nowcoder.com/practice/2baf799ea0594abd974d37139de27896?tpId=117&tqId=37777&rp=1&ru=%2Fta%2Fjob-code-high&qru=%2Fta%2Fjob-code-high%2Fquestion-ranking
# -*- coding:utf-8 -*-

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 将给定数组排序
# @param arr int整型一维数组 待排序的数组
# @return int整型一维数组
#


class Solution1:
    # bubble sort
    # 两次循环 复杂度O(n*(n-1)) = O(n)
    def MySort(self, arr):
        # write code here
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr


class Solution2:
    # selection sort
    # 两次循环 复杂度O(n*(n-1)) = O(n)
    def MySort(self, arr):
        for i in range(0, len(arr)):
            minindex = i
            for j in range(i+1, len(arr)):
                if arr[minindex] > arr[j]:
                    minindex = j
            temp = arr[i]
            arr[i] = arr[minindex]
            arr[minindex] = temp
        return arr


class Solution:
    # Insertion-Sort
    def MySort(self, arr):
        for i in range(1, len(arr)):
            pre_index = i - 1
            curr = arr[i]
            while pre_index >= 0 and curr < arr[pre_index]:
                arr[pre_index+1] = arr[pre_index]
                pre_index -= 1
            arr[pre_index+1] = curr
        return arr


s = Solution()
a = [5, 2, 3, 1, 4]
print(s.MySort(a))
