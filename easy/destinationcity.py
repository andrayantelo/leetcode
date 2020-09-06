"""
You are given the array paths, where paths[i] = [cityAi, cityBi]
means there exists a direct path going from cityAi to cityBi.
Return the destination city, that is, the city without any path
outgoing to another city.

It is guaranteed that the graph of paths forms a line without
any loop, therefore, there will be exactly one destination city.

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo"
city which is the destination city. Your trip consist of
: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Input: paths = [["A","Z"]]
Output: "Z"
"""

import unittest

class Solution:
    def destCity(self, paths):
        # return the city that has no path outgoing to another city
        # make a dictionary with keys corresponding to departure city
        # and values are the destination cities

        paths_dict = {}
        for path in paths:
            paths_dict[path[0]] = path[1]
        for path in paths:
            if path[1] not in paths_dict.keys():
                return path[1]

class TestDestCity(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_one_path(self):
        paths = [["A", "Z"]]
        self.assertEqual(self.solution.destCity(paths), "Z")

    def test_letter_paths(self):
        paths = [["B","C"],["D","B"],["C","A"]]
        self.assertEqual(self.solution.destCity(paths), "A")
    
    def test_cities(self):
        paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
        self.assertEqual(self.solution.destCity(paths), "Sao Paulo")

if __name__ == "__main__":
    unittest.main()
