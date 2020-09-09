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

# *** answer in lines 18 - 20 is incorrect for the way it's currently written***
# Complexity O(mn) where m is the length of the prefix, and 
# n is the length of the list of words we will be checking to 
# see if they have the prefix
import unittest

class Solution:
    def common_prefix(self, words):
        prev_prefix = ""
        find_prefix = ""
        # need a check for empty words array
        if not len(words):
            return prev_prefix
        # build the prefix using the first word in the words array
        for i, letter in enumerate(words[0]): 
            find_prefix = "".join([find_prefix, words[0][i]])  # This line is m^2 because
            # join will iterate over prefix again each time it adds a new letter
            # check this prefix against the rest of the words in the array
            for j in range(1, len(words)):
                # startswith method
                #if words[j][:i + 1] != find_prefix:
                if not words[j].startswith(find_prefix):
                    return prev_prefix
            prev_prefix = find_prefix
        return find_prefix

    # This is O(m*n) where m is the length of the prefix and n is the
    # length of the words array
    def find_prefix(self, words):
        # Does every word in words have the same prefix? Is their first letter
        # equal, is their second letter equal, etc
        if not words:
            return ""

        prefix = words[0]
        for i,letter in enumerate(prefix):
            for word in words[1:]:
                try:
                    if word[i] != letter:
                        return prefix[:i]
                except IndexError:
                    print('index out of range')
                    return prefix[:i]
        return prefix

class TestCommonPrefix(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_prefix(self):
        cases = [
            ['', []],
            ['ban', ['banana', 'bandana', 'bank']],
            ['', ['a', 'b']],
            ['ball', ['ball']],
            [' ', [' ']]
        ]

        for expected, words in cases:
            self.assertEqual(expected, self.solution.find_prefix(words))

    def test_no_words(self):
        words = []
        self.assertEqual(self.solution.find_prefix(words), "")

    def test_one_word(self):
        words = ["flower"]
        self.assertEqual(self.solution.find_prefix(words), "flower")

    def test_one_letter_word(self):
        words = ["a"]
        self.assertEqual(self.solution.find_prefix(words), "a")

    def test_one_letter_words(self):
        words = ["a", "apple", "aardvark", "adolescence"]
        self.assertEqual(self.solution.find_prefix(words), "a")
        words = ["a", "aaagh", "aaaha", "aaron"]
        self.assertEqual(self.solution.find_prefix(words), "a")
    
    def test_no_find_prefix(self):
        words = ["bowl", "car", "pool", "house"]
        self.assertEqual(self.solution.find_prefix(words), "")

    def test_same_word(self):
        words = ["apple", "apple", "apple"]
        self.assertEqual(self.solution.find_prefix(words), "apple")
        words = ["apple", "apple", "orange"]
        self.assertEqual(self.solution.find_prefix(words), "")
       

if __name__ == "__main__":
    #words = ["flower", "flow", "flight"]
    #solution = Solution()
    #print(solution.find_prefix(words))
    unittest.main()