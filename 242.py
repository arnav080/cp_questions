# Question: 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
        for n in range(len(t)):
            countT[t[n]] = 1 + countT.get(t[n], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
