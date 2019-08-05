"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
 elements are subset of nums2. Find all the next greater numbers for nums1's
  elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number
 to its right in nums2. If it does not exist, output -1 for this number.
 
Example 1
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

"""
import unittest

class Stack:
    def __init__(self, arr):
        self.stack = arr
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        return self.stack.pop()
        
    def __bool__(self):
        return bool(len(self.stack))
        
        
# the stack in the function below is just a holding place for numbers in
# the second array for which you have not found the next greater number yet

def next_greater_number(arr1, arr2):
    greater_dict = {}
    stack = []
    stack.append(float("inf"))
    
    # find all the next greater numbers for the elements in the second array (the superset)
    # and place them in the dict.
    for i in range(len(arr2)):
        while arr2[i] > stack[-1]:
            greater_dict[stack[-1]] = arr2[i]
            stack.pop()
        stack.append(arr2[i])
    
    result = [greater_dict.get(arr1[i], -1) for i in range(len(arr1))]
    return result
    
class TestGreaterNumber(unittest.TestCase):
    
    def test_case1(self):
        nums1 = [4,1,2]
        nums2 = [1,3,4,2]
        self.assertEqual(next_greater_number(nums1, nums2), [-1,3,-1])
    
    
    
        
if __name__ == "__main__":
    s = Stack(['h','e','l','l','o'])
    unittest.main()
    next_greater_number([2, 4], [1, 2, 3, 4])
