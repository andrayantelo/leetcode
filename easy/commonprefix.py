"""
Write a function to find the longest common prefix
string amongst an array of strings.

If there is no common prefix, return an empty string "".

Examples:

Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

# Complexity O(mn) where m is the length of the prefix, and 
# n is the length of the list of words we will be checking to 
# see if they have the prefix
import unittest

class Solution:
    def common_prefix(self, words):
        # need a check for empty words array
        prev_prefix = ""
        common_prefix = ""
        if not len(words):
            return prev_prefix
        for i, letter in enumerate(words[0]):
            common_prefix = "".join([common_prefix, words[0][i]])  # n^2
            for j in range(1, len(words)):
                # startswith method
                #if words[j][:i + 1] != common_prefix:
                if not words[j].startswith(common_prefix):
                    return prev_prefix
            prev_prefix = common_prefix
        return common_prefix

class TestCommonPrefix(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_no_words(self):
        words = []
        self.assertEqual(self.solution.common_prefix(words), "")

    def test_one_word(self):
        words = ["flower"]
        self.assertEqual(self.solution.common_prefix(words), "flower")

    def test_one_letter_word(self):
        words = ["a"]
        self.assertEqual(self.solution.common_prefix(words), "a")

    def test_one_letter_words(self):
        words = ["a", "apple", "aardvark", "adolescence"]
        self.assertEqual(self.solution.common_prefix(words), "a")
        words = ["a", "aaagh", "aaaha", "aaron"]
        self.assertEqual(self.solution.common_prefix(words), "a")
    
    def test_no_common_prefix(self):
        words = ["bowl", "car", "pool", "house"]
        self.assertEqual(self.solution.common_prefix(words), "")

    def test_same_word(self):
        words = ["apple", "apple", "apple"]
        self.assertEqual(self.solution.common_prefix(words), "apple")
        words = ["apple", "apple", "orange"]
        self.assertEqual(self.solution.common_prefix(words), "")
       

if __name__ == "__main__":
    #words = ["flower", "flow", "flight"]
    #solution = Solution()
    #print(solution.common_prefix(words))
    unittest.main()