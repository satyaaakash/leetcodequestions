class Solution:
    def solve(self, board: List[List[str]]) -> None:
        \\\
        Do not return anything, modify board in-place instead.
        \\\
        if not board or not board[0]:
            return
        
        rows, cols = len(board),len(board[0])

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=\O\:
                return
            board[r][c]=\S\
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(r+dr, c+dc)
                

        

        for r in range(rows):
            dfs(r,0)
            dfs(r, cols-1)
        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)

        for i in range(rows):
            for j in range(cols):
                if board[i][j]==\O\:
                    board[i][j]=\X\
                elif board[i][j]==\S\:
                    board[i][j]=\O\
        
