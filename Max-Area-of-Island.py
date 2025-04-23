class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows,cols =len(grid),len(grid[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]==0:
                return 0
            else:
                grid[i][j]=0
                area = 1 
                area += dfs(i+1,j)
                area+=dfs(i-1,j)
                area+=dfs(i,j+1)
                area+=dfs(i,j-1)
            return area
        
        max_area =0 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    max_area = max(max_area,dfs(i,j))
        return max_area

        