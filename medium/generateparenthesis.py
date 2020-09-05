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
        # base case
        if n == 1:
            return "()"
        
        inner = "(" + self.generateParenthesis(n-1) + ")"
        print(inner)
        #left = "()" + self.generateParenthesis(n-1)
        #right = self.generateParenthesis(n-1) + "()"

        
        #results.append("(" + "".join(self.generateParenthesis(n - 1)) + ")")
        #results.append("()" + "".join(self.generateParenthesis(n - 1)))
        #results.append("".join(self.generateParenthesis(n - 1)) + "()")


class TestGenerateParenthesis(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

if __name__ == "__main__":
    solution = Solution()
    n = 3
    print(solution.generateParenthesis(n))
        