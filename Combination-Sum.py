class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #initialized a result list to store 
        result = []
        #defined a function backtrack with states --> start_index , current combination and current sum 
        def backtrack(start_index,curr_comb, curr_sum):
            #base condition 1 , if current sum is equal to target then store it in result and return
            if curr_sum == target:
                result.append(curr_comb[:])
                return
            #base case2: if current sum is greater than target then no need to go further so stop 
            if curr_sum>target:
                return
            #if not above cases then start recursive through for loop for all the candidate options avaliable to pick
            for i in range(start_index,len(candidates)):
                #make that choice i.e append the avaiable candidate and backtrack it 
                curr_comb.append(candidates[i])
                #backtrack it recursively with current sum updated to candidate[i]+current_Sum
                backtrack(i,curr_comb,curr_sum+candidates[i])
                #at last undo that choice with pop from current_combination
                curr_comb.pop()
        #start the backtracking with 0th candidate 
        backtrack(0,[],0)
        #return the result
        return result

        