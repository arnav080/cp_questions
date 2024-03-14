'''
Question:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        
        sCount = sorted(count.items(), key = lambda item:item[1],reverse = True)

        for i in range(k):
            res.append(sCount[i][0])
        
        return res
