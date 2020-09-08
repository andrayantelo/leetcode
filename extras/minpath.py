"""Given a m x n grid filled with non-negative numbers,
 find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

import timeit
import collections

class Solution:
    def minPathSum(self, grid):
        
        memo = collections.defaultdict(lambda: 0)
        
        def inner(grid, r, c):
            print("r: {}".format(r))
            print("c: {}".format(c))
            print("len(grid): {}".format(len(grid)))
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                print("reached base case")
                print("r: {}".format(r))
                print("c: {}".format(c))
                print(len(grid))
                return grid[r][c]
                
            curVal = grid[r][c]
            
            
            if memo[(r, c)]:
                print("alredy in memo")
                return memo[(r, c)]
            if r + 1 >= len(grid) and c + 1 <= len(grid[0]):
                
                 
                print("nothing below")
                memo[(r, c)] = inner(grid, r, c+1) + curVal
                return inner(grid, r, c+1) + curVal
            if c + 1 >= len(grid[0]) and r + 1 <= len(grid):
                
                print("nothing to the right")
                memo[(r, c)] = inner(grid, r+1, c) + curVal
                return inner(grid, r+1, c) + curVal
            
            
            memo[(r, c)] = min(inner(grid, r+1, c), inner(grid, r, c+1)) + curVal
            return min(inner(grid, r+1, c), inner(grid, r, c+1)) + curVal
        
        minPath = inner(grid, 0, 0)
        return minPath
        
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.minPathSum( [
                                [1,3,1],
                                [1,5,1],
                                [4,2,1]
                               ])
                               )
                               
    timeit.timeit(solution.minPathSum( [
                                [1,3,1],
                                [1,5,1],
                                [4,2,1]
                               ])
                  )
                               
    #print(solution.minPathSum([[1,2,5],
    #                           [3,2,1]]))
    
    #[[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
    #[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
    #[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
    #[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
    #[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
    #[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
        
