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
            if my_var > 1:
                carry_over = 1
                c.append(0)
            else:
                c.append(my_var)
        if carry_over:
            c.append(carry_over)
        # reverse c
        return c[::-1]

    def bin_add_diff(self, a, b):
        pass

    def bin_add_str(self, a, b):
        pass

class TestBinaryAdd(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_standard(self):
        a = [1, 1, 1]
        b = [1, 0, 0]

        self.assertEqual(self.solution.bin_add_same(a, b), [1, 0, 1, 1])

    def test_empty(self):
        self.assertEqual(self.solution.bin_add_same([],[]), [])

if __name__ == "__main__":
    unittest.main()
    #a = [1, 1, 1]
    #b = [1, 0, 0]

    #solution = Solution()
    #print(solution.bin_add(a, b))