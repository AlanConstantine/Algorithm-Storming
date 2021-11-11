class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0
        if len(points) == 1:
            return 1
        res = 1
        points.sort(key=lambda x: x[1])
        end = points[0][-1]
        for b_index in range(1, len(points)):
            if end < points[b_index][0]:
                res += 1
                end = points[b_index][1]
        return res


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
# points = [[1, 2], [3, 4], [5, 6], [7, 8]]
# points = [[1, 2], [2, 3], [3, 4], [4, 5]]
# points = [[1, 2]]
points = [[2, 3], [2, 3]]

print(Solution().findMinArrowShots(points))
