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

    cache = {}

    def generateParenthesis(self, n):
        if n in self.cache:
            return self.cache[n]
        results = []
        # base case
        if n == 0:
            return [""]
        
        for k in range(1, n):
            lefts = self.generateParenthesis(k)
            rights = self.generateParenthesis(n - k)
            for left in lefts:
                for right in rights:
                    results.append(left + right)
        for parenthesis in self.generateParenthesis(n - 1):
            middle = "(" + parenthesis  + ")"
            results.append(middle)
        
        self.cache[n] = sorted(set(results))
        return self.cache[n]


class TestGenerateParenthesis(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

if __name__ == "__main__":
    solution = Solution()
    n = 3
    print(len(solution.generateParenthesis(n)))
    for i in range(5):
        print(len(solution.generateParenthesis(i)))
        