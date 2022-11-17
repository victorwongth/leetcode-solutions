class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        count: int = 0
        for i, row in enumerate(grid):
            for j, column in enumerate(row):
                if column == "0":
                    continue
                else:
                    count += 1
                    self.setZero(grid, i+1, j)
                    self.setZero(grid, i-1, j)
                    self.setZero(grid, i, j+1)
                    self.setZero(grid, i, j-1)
        return count


    def setZero(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:        
            return         
        if grid[i][j] == "0":        
            return        
        if grid[i][j] == "1":        
            grid[i][j] = "0"        
            self.setZero(grid, i+1, j)        
            self.setZero(grid, i-1, j)        
            self.setZero(grid, i, j+1)        
            self.setZero(grid, i, j-1)        
            return        
