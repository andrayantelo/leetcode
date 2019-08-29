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

class Solution:
    def nextGreaterElements(self, nums):
        print("Looking for next greater elements")
        greater_elements = {}
        great = []
        stack = []
        stack.append(float("inf"))
        
        nums = list(enumerate(nums))
        i = 0
        # iterate over array to look at each element one by one
        while i < len(nums):
            print("i: {}".format(i))
            current_element = nums[i][1]
            print("current_element: {}".format(current_element))
            prev_el_index = nums[i][0] - 1
            print("prev_el_index: {}".format(prev_el_index))
            # we'll want to re-iterate over the array up to i but only
            # if we didn't find the next greater element between our
            # current element and the last element
            
            # so everything can be the same except when nums[i][1] is not
            # greater than stack [-1]
            print("stack[-1]: {}".format(stack[-1]))
            
            
            while current_element > stack[-1] and i!= prev_el_index:
                greater_elements[stack[-1]] = current_element
                great.append((stack[-1], current_element))
                print('great so far: {}'.format(great))
                stack.pop()
            
            # check if we made it to the last element, if yes
            # then we want to start over with the loop
            if i == (len(nums) - 1):
                print('restarting loop')
                
                i = 0
            
            # but when do we break? when we have attempted to look for the
            # next greater element of each element. How do we know this?
            # keep a seen array? TODO WHEN TO BREAK. DO NOT RUN
            # you break when your index is back to being the index of the 
            # element whose next greater element you are looking for?
            
            stack.append(current_element)
            print("stack: {}".format(stack))
            i += 1
        print(greater_elements)
        print(great)
                
        
        
        
        
if __name__ == '__main__':
    
    nums1 = [1, 2, 1]
   
    
    result = Solution()
    result.nextGreaterElements(nums1)
    

