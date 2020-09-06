"""
Given a string, you need to reverse the order of characters
in each word within a sentence while still preserving whitespace
and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""

import unittest

class Solution:
    def reverseWords(self, s):
        s = s.split(" ")
        result = []
        for word in s:
            word = "".join(reversed(word))
            result.append(word)
        return " ".join(result)

class TestReverseWords(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_standard(self):
        str = "Let's take LeetCode contest"
        self.assertEqual(self.solution.reverseWords(str), "s'teL ekat edoCteeL tsetnoc")

if __name__ == "__main__":
    unittest.main()
        

