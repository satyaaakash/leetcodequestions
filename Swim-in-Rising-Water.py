class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        visited = set()

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        min_heap =[(grid[0][0],0,0)]

        while min_heap:

            time, row, col = heapq.heappop(min_heap)

            if (row,col) in visited:
                continue
            visited.add((row,col))

            if row==n-1 and col==n-1:
                return time
            
            for neirow,neicol in directions:
                new_row = neirow+row
                new_col = neicol+col

                if 0<=new_row<n and 0<=new_col<n and (new_row,new_col) not in visited:
                    next_time = max(time, grid[new_row][new_col])
                    heapq.heappush(min_heap,(next_time,new_row,new_col))
        return -1