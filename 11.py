'''
Question:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxArea = 0
        l = 0
        r = n - 1

        while l < r:
            # Area of a rectangle is length * breath
            width = r - l
            area = min(height[l], height[r]) * width
            maxArea = max(maxArea, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea
        
