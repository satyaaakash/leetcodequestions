class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        if not board or not board[0]:
            return False
        
        def backtrack(r,c,index):
            # If we've matched all letters in 'word', we are done!

            if index == len(word):
                return True
            # If out of bounds or not matching the needed character, fail fast
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=word[index]:
                return False
              # Temporarily mark the current cell as used (e.g., '#')
            temp = board[r][c]
            board[r][c]='#'
            # Check all 4 directions for the next letter
            # (up, down, left, right)
            found = (backtrack(r-1,c,index+1) or backtrack(r+1,c,index+1) or backtrack(r,c-1,index+1) or backtrack(r,c+1,index+1))
             # Restore the cell's original value (unmark)
            board[r][c]=temp

            return found
# Try starting from each cell in the board
        for row in range(rows):
            for col in range(cols):
                if board[row][col]==word[0]: # Potential starting point
                    if backtrack(row,col,0):
                        return True
        return False
        