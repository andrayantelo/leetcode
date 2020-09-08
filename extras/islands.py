"""Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""  

class Solution(object):
    def get_land_neighbors(self, i, j, grid):
        """
        :type i: int
        :type j: int
        :type grid: List[List[str]]
        :rtype: List(tup(int(ni), int(nj)))
        """
        output = []
        # for all of the neighbors ni, nj of i, j
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if (0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == "1"):
                output.append((ni, nj))
        return output
                
            
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_islands = 0
        # set containing tuples which contain coordinates of plots of land we
        # have already seen in our traversal of the grid
        seen = set()
        
        for i in range(len(grid)):
            row = grid[i]
            
            for j in range(len(row)):
                # if this plot is land and we haven't seen it yet
                if grid[i][j] == "1" and (i, j) not in seen:
                    # add the coordinates to our seen set
                    seen.add((i,j))
                    
                    # find the land neighbors of this current island, to see
                    # how big this island actually is
                    
                    neighbors = self.get_land_neighbors(i, j, grid)
                    
                    # for the neighbors that you have found, find THEIR land neighbors
                    # as well, untill you have found the whole island
                    while neighbors:
                        current = neighbors.pop()
                        
                        if current in seen:
                            continue
                        else:
                            neighbors.extend(self.get_land_neighbors(*current, grid))
                            seen.add(current)
                    # assume we have found an island and increment counter
                    num_islands += 1
                            
        return num_islands
                    
                    
                    


def main():
    
    sample= """
            11000
            11000
            00100
            00011 """

    result = 3
    sample = sample.strip().split()
    
    num_islands = Solution()
    num_islands.numIslands(sample)
    
    sample1 = """
              10010
              01100
              01001
              01111"""
              
    sample1 = sample1.strip().split()
    num_islands.numIslands(sample1)
    
    sample2 = """
              11110
              11010
              11000
              00000
              """
    sample2 = sample2.strip().split()
    num_islands.numIslands(sample2)
    
    
if __name__ == "__main__":
    main()
