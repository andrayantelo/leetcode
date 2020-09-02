"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Examples:

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
"""

import unittest

class Solution:
    def isValid(self, s):
        stack = []
        opening_chars = ["(", "{", "["]
        pairs = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for element in s:
            # if there's nothing on the stack, and s is one of
            # (, {, [
            if not len(stack) or element in opening_chars:
                # place element on the stack
                stack.append(element)
            # if we have a closing_char we need to compare with what
            # is at the top of the stack
            else:
                # if the corresponding opening char is at the top of stack
                # then we good, remove that from the stack and continue
                if stack[-1] == pairs[element]:
                    stack.pop()
                else:
                    #not valid
                    return False
        # if stack empty, then valid
        if not len(stack):
            return True
        else:
            return False
        



class TestIsValid(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_standard(self):
        self.assertTrue(self.solution.isValid("()"))

    def test_multiple(self):
        self.assertTrue(self.solution.isValid("()[]{}"))

    def test_standard_false(self):
        self.assertFalse(self.solution.isValid("(]"))

    def test_multiple_false(self):
        self.assertFalse(self.solution.isValid("([)]"))

    def test_nested(self):
        self.assertTrue(self.solution.isValid("{[]}"))
    
    def test_one_opening_char(self):
        self.assertFalse(self.solution.isValid("("))

    def test_one_closing_char(self):
        self.assertFalse(self.solution.isValid(")"))

if __name__ == "__main__":
    #solution = Solution()
    #s = ""
    #solution.isValid(s)
    #s = "()[]{}"
    #solution.isValid(s)
    #s = "(]"
    #solution.isValid(s)
    unittest.main()
