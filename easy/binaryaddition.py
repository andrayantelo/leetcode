""" assume binary numbers a and b are of equal length.
they are given in this form a = [1, 1, 1] b = [1, 0, 0].
result should be c = [1, 0, 1, 1]
"""

import unittest

class Solution():

    # assumes a and b are the same length
    def bin_add_same(self, a, b):
        c = []
        carry_over = 0
        # iterate in reverse over a and b
        for i in range(len(a) - 1, -1, -1):
            my_var = a[i] + b[i] + carry_over
            # if result > 1, you have a carry over
            carry_over = 1 if my_var > 1 else 0
            c.append(my_var % 2)
        if carry_over:
            c.append(carry_over)
        # c was built backwards so reverse it
        c.reverse()
        return c
    
    # version where a and b are given as arrays and can be different lengths
    def bin_add_diff(self, a, b):
        # the same as before except iterate over the smaller one
        c = []
        carry_over = 0
        # make a be the smaller one
        a, b = sorted([a, b], key=len)
        # pad a so that a and b are the same length
        padding = len(b) - len(a)
        a = [0]*padding + a
        for i in range(len(b) - 1, -1, -1):
            my_var = a[i] + b[i] + carry_over
            # if result > 1, you have a carry over
            carry_over = 1 if my_var > 1 else 0
            c.append(my_var % 2)
        if carry_over:
            c.append(carry_over)
        # reverse c
        c.reverse()
        return c 
    
    # version where a and b are given as string and can be of different lengths
    def bin_add_str(self, a, b):
        # make a be the smaller one so that we don't have to
        # do a bunch of if-else statements to figure it out
        a, b = sorted([a, b], key=len)
        # pad a with 0's so that a and b are the same length
        a = a.zfill(len(b))
        c = ""
        carry_over = 0
        for i in range(len(b) - 1, -1, -1):
            my_var = int(a[i]) + int(b[i]) + carry_over
            # if result > 1, you have a carry over
            carry_over = 1 if my_var > 1 else 0
            c = c + str(my_var % 2)
        if carry_over:
            c = c + str(carry_over)
        # reverse c
        c = c[::-1]
        return c


class TestBinaryAdd(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_standard(self):
        a = [1, 1, 1]
        b = [1, 0, 0]

        self.assertEqual(self.solution.bin_add_same(a, b), [1, 0, 1, 1])
        a = [1, 1, 1]
        b = [1, 0]
        self.assertEqual(self.solution.bin_add_diff(a, b), [1, 0, 0, 1])
        b = [1, 1, 1]
        self.assertEqual(self.solution.bin_add_same(a, b), [1, 1, 1, 0])
        b = [1, 1]
        self.assertEqual(self.solution.bin_add_diff(a, b), [1, 0, 1, 0])

    def test_empty(self):
        self.assertEqual(self.solution.bin_add_same([],[]), [])
        self.assertEqual(self.solution.bin_add_diff([], []), [])

    def test_bin_str(self):
        a = "111"
        b = "100"
        self.assertEqual(self.solution.bin_add_str(a, b), "1011")
        a = "111"
        b = "10"
        self.assertEqual(self.solution.bin_add_str(a, b), "1001")
        b = "111"
        self.assertEqual(self.solution.bin_add_str(a, b), "1110")
        b = "11"
        self.assertEqual(self.solution.bin_add_str(a, b), "1010")
        self.assertEqual(self.solution.bin_add_str("", ""), "")

if __name__ == "__main__":
    unittest.main()
    #a = [1, 1, 1]
    #b = [1, 0, 0]

    #solution = Solution()
    #print(solution.bin_add(a, b))
    #a = [1, 1, 1]
    #b = [1, 0]
    #print(solution.bin_add_diff(a, b))

    #a = "111"
    #b = "100"
    #print(solution.bin_add_str(a, b))
    