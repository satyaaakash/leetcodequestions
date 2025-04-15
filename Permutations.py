class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result =[]

        def backtrack(start):
            #base case : when start completes the iteration through the nums , need to append that to result
            if len(nums)==start:
                result.append(nums[:])
                return
            #recursive case
            for i in range(start,len(nums)):
                #swap ith element and start element (make that choice)
                nums[start],nums[i]=nums[i],nums[start]
                #backtrack it after swapping and complete it
                backtrack(start+1)
                #undo the choice was made , so swap again
                nums[start],nums[i]=nums[i],nums[start]
        #call first element from nums to start the process
        backtrack(0)
        #return the result
        return result
        