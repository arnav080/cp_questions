'''
Question:
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
'''

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for x in words:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        res = sorted(freq, key=lambda x: (-freq[x], x))
        return res[:k]
