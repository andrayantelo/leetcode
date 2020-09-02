"""
Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
import unittest

class Solution:
    def generateParenthesis(self, n):
        available_open = n - 1
        available_closed = n
        size_of_string = n*2

        results = []
        curr_result = ["("]

        for i in range(1, size_of_string):
            if curr_result[i - 1] == "(" and available_open > 0:
                 

class TestGenerateParenthesis(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

if __name__ == "__main__":
    solution = Solution()
    n = 3
    solution.generateParenthesis(n)
        