# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

# 你需要按照以下要求，帮助老师给这些孩子分发糖果：

# 每个孩子至少分配到 1 个糖果。
# 评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
# 那么这样下来，老师至少需要准备多少颗糖果呢？

#  

# 示例 1：

# 输入：[1,0,2]
# 输出：5
# 解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。


class Solution:
    def candy(self, ratings):
        if len(ratings) < 2:
            return len(ratings)
        res = [1] * len(ratings)  # 每人至少一颗糖，所以根据人数初始化每个人手上的糖果

        i = 1
        while i < len(ratings):
            # 从左向右遍历，如果当前小孩评分大于左边小孩，那么当前小孩的糖果为左边小孩糖果+1，以保证当前小孩手上的大于左边的小孩
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
            i += 1
        i = len(ratings)-1
        while i-1 >= 0:
            # 从右向左遍历，如果左边小孩评分大于当前小孩
            if ratings[i] < ratings[i-1]:
                res[i-1] = max(res[i-1], res[i]+1)  # 则再判断左边的小孩的糖果数是否已经大于当前小孩的
            i -= 1
        return sum(res)


print(Solution().candy([1, 0, 2]))
