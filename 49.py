'''
Question: 
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cMap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord("a")] += 1
        
            cMap[tuple(count)].append(s)
        return cMap.values()
