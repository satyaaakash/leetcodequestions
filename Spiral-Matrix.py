class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        #time and space: O(m*n)
        result =[]

        if not matrix:
            return result
        
        top, left = 0,0
        bottom, right = len(matrix), len(matrix[0])

        while left<right and top<bottom:
            #top : from. left to right 
            for i in range(left,right):
                result.append(matrix[top][i])
            top+=1

            #right column : from top to bottom 

            for i in range(top,bottom):
                result.append(matrix[i][right-1])
            right-=1

            #bottom: right to left 
            if top<bottom:
                for i in range(right-1,left-1,-1):
                    result.append(matrix[bottom-1][i])
                bottom-=1
            
            #left:bottom to top
            if left<right:
                for i in range(bottom-1,top-1,-1):
                    result.append(matrix[i][left])
                left+=1
        return result

        