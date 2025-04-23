class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        # first set up queue and set for both pacific and atlantic ocean . while we are doing BFS for this 

        pacific_queue = deque()
        pacific_seen = set()

        atlantic_queue = deque()
        atlantic_seen = set()

        rows, cols = len(heights), len(heights[0])

        #now append all the left edge and top- edge elements to pacific , bottom most and right most to atlantic

        #for top edge elements to pacific:
        for j in range(cols):
            pacific_queue.append((0,j))
            pacific_seen.add((0,j))
        #for left most elements to pacific :
        for i in range(rows):
            pacific_queue.append((i,0))
            pacific_seen.add((i,0))
        #for bottom most to atlantic

        for j in range(cols):
            atlantic_queue.append((rows-1,j))
            atlantic_seen.add((rows-1,j))
        #for right most elements to atlantic

        for i in range(rows):
            atlantic_queue.append((i,cols-1))
            atlantic_seen.add((i,cols-1))

        #now start the bfs process 
        #define a function to get the coordinates of water flows becuase we can call it two times (one for pacific and another for atlantic)

        def get_coords(queue,seen):

            while queue:
                row,col = queue.popleft()
                #standard procedure to traverse neighbor elements from that element 
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_row = row+dr
                    new_col =col+dc
                    #condition is if the neighbor elements height is greater than present height then water will flow and also we check whether that element is already seen or not.
                    if 0<=new_row<rows and 0<=new_col<cols and heights[new_row][new_col]>=heights[row][col] and (new_row,new_col) not in seen:
                        queue.append((new_row,new_col))
                        seen.add((new_row,new_col))
        
        #now call get_coords function with pacific and atlantic

        get_coords(pacific_queue, pacific_seen)
        get_coords(atlantic_queue,atlantic_seen)

        return list(pacific_seen & atlantic_seen) #output should be a list of coordinates where water flows to both pacific ocean and atlantic ocean 

        