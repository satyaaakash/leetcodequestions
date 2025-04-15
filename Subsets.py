class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(i,subset):
            result.append(subset[:])
                
            
            for i in range(i,len(nums)):
                subset.append(nums[i])
                backtrack(i+1,subset)
                subset.pop()

        backtrack(0,[])
        return result
     
        










        # #initialize a empty array to store result 
        # result =[]
        # #also initialize another array to store subset
        # subset = []

        # #define another function for recursive call backtrakcing
        # def backtrack(i):
        #     #check valid condition or base condition
        #     if i==len(nums):
        #         result.append(subset[:]) #store the result at the dead end whatever you have 
        #         return
        #     #if not then add that element to subset and backtrack till you rach dead end
        #     subset.append(nums[i])
        #     #after appending perform backtracking recursive call with that decision
        #     backtrack(i+1)
        #     #if not that decision, pop out the that number and backtrack again
        #     subset.pop()
        #     backtrack(i+1)
        # #strat with i=0
        # backtrack(0)
        # return result
        