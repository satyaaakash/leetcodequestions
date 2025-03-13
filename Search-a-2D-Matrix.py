class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #rows and cols are len(matrix ) and len(matrix[0]) 
        rows = len(matrix)
        cols = len(matrix[0])

        #initialize that low and high as we do for binary search questions
        low = 0
        high = rows*cols-1 #i.e last element from the 2d array

        while low <=high:
            mid = low+(high-low)//2
            row = mid//cols #this gives which row is the mid element 
            col = mid%cols #this gives which col is in the mid element
            #now compare target with mid element and update the low and high as you do 
            if target>matrix[row][col]:
                low =mid+1
            elif target<matrix[row][col]:
                high =mid-1
            else:
                return True
        return False
        