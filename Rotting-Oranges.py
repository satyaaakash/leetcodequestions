from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])

        fresh = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c,0))
                elif grid[r][c]==1:
                    fresh+=1
        time =0
        while queue:
            row,col,minute = queue.popleft()
            time = minute
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_row = row+dr
                new_col = col+dc
                if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]==1:
                    grid[new_row][new_col]=2
                    fresh -= 1
                    queue.append((new_row,new_col,minute+1))
        return time if fresh ==0 else -1 

        