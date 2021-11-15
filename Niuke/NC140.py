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


class Solution3:
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


class Solution4:
    # shell-Sort
    # link: https://www.youtube.com/watch?v=PnxGnuItVuE
    def MySort(self, arr):
        gap = len(arr) // 2  # 定义步长
        while gap >= 1:
            for i in range(gap, len(arr)):
                crr = arr[i]  # i 指向子序列中的最后一个元素
                j = i - gap  # j 指向子序列中的第一个元素
                while j >= 0 and crr < arr[j]:
                    # 当j大于零且子序列中的最后一个元素小于第一个元素，发生交换
                    arr[j+gap] = arr[j]
                    j = j - gap
                arr[j+gap] = crr
            gap = gap // 2
        return arr


class Solution:
    def MySort(self, arr):
        pass


class Solution:
    def MySort(self, arr):
        self.quicksort(arr, 0, len(arr))
        return arr

    def quicksort(self, arr, s, e):
        if s >= e:
            return
        pivot = arr[s]
        i, j = s, e
        while i != j:
            while i < j and arr[i] <= pivot:
                i += 1
            self.swap(arr[i], arr[j])
            while i < j and arr[j] >= pivot:
                j -= 1
            self.swap(arr[i], arr[j])
        self.quicksort(arr, s, i-1)
        self.quicksort(arr, i+1, e)

    def swap(self, a, b):
        a, b = b, a
        return a, b


s = Solution()
a = [5, 2, 3, 1, 4]
print(s.MySort(a))
