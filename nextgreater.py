"""
    Given a circular array (the next element of the last element is the first
    element of the array), print the Next Greater Number for every element.
    The Next Greater Number of a number x is the first greater number to its
    traversing-order next in the array, which means you could search circularly
    to find its next greater number. If it doesn't exist, output -1 for this number.
    
    Example: 
    Input: [1, 2, 1]
    Output: [2, -1, 2]
    
    Explanation: The first 1's next greater number is 2; 
    The number 2 can't find next greater number; 
    The second 1's next greater number needs to search circularly, which is also 2.
"""

import unittest
from itertools import chain, repeat

class Solution:
    def nextGreaterElements(self, nums):
        stack = [(0, float('inf'))]
        ng = {}
        output = []
        for (i, num) in enumerate(nums):
            while num > stack[-1][1]:
                ng[stack[-1]] = num
                stack.pop()
            stack.append((i, num))
        for (i, num) in enumerate(nums):
            while num > stack[-1][1]:
                ng[stack[-1]] = num
                stack.pop()
            if (i, num) in ng:
                output.append(ng[(i, num)])
            else:
                output.append(-1)

                
        return output


class TestNextGreater(unittest.TestCase):
    
    def __init__(self):
        self.nextGreater = Solution()
        
    
    def test_standard(self):
        self.assert_equal(self.nextGreater.nextGreaterElements([1, 2, 1]), [2, -1, 2])
        
        
        
if __name__ == '__main__':
    
    nums1 = [1, 2, 1]
   
    
    result = Solution()
    print(result.nextGreaterElements(nums1))
    nums2 = [3, 4, 1, 3, 5]
    print(result.nextGreaterElements(nums2))
    
"""
    itertools.cycle to construct a blackbox (enumerate(nums)) is a blackbox
"""
    

