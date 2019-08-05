"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
 elements are subset of nums2. Find all the next greater numbers for nums1's
  elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number
 to its right in nums2. If it does not exist, output -1 for this number.

"""

class Stack:
    def __init__(self, arr):
        self.stack = arr
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        return self.stack.pop()
        
    def __bool__(self):
        return bool(len(self.stack))
        
if __name__ == "__main__":
    s = Stack(['h','e','l','l','o'])
    
    print(s.pop())
    print(bool(s))
    s.push('w')
    print(s.stack)
