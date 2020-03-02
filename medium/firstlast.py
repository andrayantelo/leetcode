"""
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution:
    def searchRange(self, nums, target):
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        if not len(result):
            result = [-1,-1]
        return [result[0], result[-1]]

if __name__ == "__main__":
    solution = Solution()
    nums = [5, 7, 7, 8, 8,8, 10]
    target = 8
    print(solution.searchRange(nums, target))
    target = 6
    print(solution.searchRange(nums, target))
    target = 10
    print(solution.searchRange(nums, target))