# Question: 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        for x in s:
            count[ord(x) - ord('a')] += 1 

        for x in t:
            count[ord(x) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False

        return True
