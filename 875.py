'''
Question:

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            middle = (left +  right) // 2
            hours = 0
            for x in piles:
                hours += math.ceil(x / middle)

            if hours <= h:
                res = min(res, middle)
                right = middle - 1
            else:
                left = middle + 1

        return res

# [3,6,7,11] h=8
# left = 1, right = 11, middle = 6
# 3/6 = 1, 1, 2, 2
# sum = 6 < 8 True
# middle - 1
# 3/5 = 1, 2, 2, 3
# sum = 8 True
# middle - 1 
# 3/4 = 1 + 2 + 2 + 3
# sum = 8, True
# middle - 1 {3}
# 1, 2, 3, 4
#return
#  [6, 5, 4]
