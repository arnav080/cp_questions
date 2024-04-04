'''
Question:
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countMag = {}
        
        for c in magazine:
            if c in countMag:
                countMag[c] += 1
            else:
                countMag[c] = 1

        for char in ransomNote:
            if char in countMag and countMag[char] > 0:
                countMag[char] -= 1
            else:
                return False
        return True
