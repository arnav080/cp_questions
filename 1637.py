'''
Question:
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.
A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.
Note that points on the edge of a vertical area are not considered included in the area.
'''

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)
        d = []
        for l in points:
            d.append(l[0])
        d.sort()
        ans = []
        for i in range(len(d) - 1):
            ans.append(d[i+1] - d[i])
        ans.sort()
        return max(ans)
