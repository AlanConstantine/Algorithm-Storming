# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

# 给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。

#  

# 示例 1：

# 输入：flowerbed = [1, 0, 0, 0, 1], n = 1
# 输出：true
# 示例 2：

# 输入：flowerbed = [1, 0, 0, 0, 1], n = 2
# 输出：false


# 利用递归进行窗口为3（pre, cur, last）的进行遍历，当窗孔内三个数满足条件的时候在cur种下花
# 即当pre=0，cur=0，last=0，cur才可以种下花，以及当pre=1，cur=0，last=0，last可以种下花
# 多考虑边界情况
class Solution1:
    flo = None
    n = None

    def canPlaceFlowers(self, flowerbed, n):
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        self.flo = flowerbed
        self.n = n
        self.help(0, -1, 1)
        return True if self.n == 0 else False

    def help(self, cur, pre, la):
        if self.n == 0:
            return
        if la == len(self.flo):
            return
        if pre == -1 and self.flo[cur] == 0 and self.flo[la] == 0:
            self.flo[cur] = 1
            self.n -= 1
        elif self.flo[cur] == 0 and self.flo[pre] == 0 and self.flo[la] == 0:
            self.flo[cur] = 1
            self.n -= 1
        if la == len(self.flo)-1 and self.flo[la] == 0 and self.flo[cur] == 0 and self.flo[pre] == 1:
            self.flo[cur+1] = 1
            self.n -= 1
            return
        self.help(cur+1, cur, la+1)


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        newfl = [0] + flowerbed + [0]  # 在花坛首位加上0进行填补来消除边界情况
        for i in range(1, len(newfl)-1):  # 遍历的时候从1开始到len(newfl)-1前结束这样就避免考虑到了填补位置
            if newfl[i] == 0 and newfl[i-1] == 0 and newfl[i+1] == 0:
                newfl[i] = 1
                n -= 1
            if n == 0:
                return True
        return False

        # flowerbed = [1, 0, 0, 0, 1]
flowerbed = [0, 1, 0]
n = 1
print(Solution().canPlaceFlowers(flowerbed, n))
