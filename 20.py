'''
Question:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {'(':')', '{':'}', '[':']'}

        for c in s:
            if c in openToClose:
                stack.append(c)
            elif len(stack) == 0 or c != openToClose[stack.pop()]:
                return False
        return len(stack) == 0
