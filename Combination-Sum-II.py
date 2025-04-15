class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       candidates.sort()
       result = []

       def backtrack(start_index,cur_comb,cur_sum):
        if cur_sum==target:
            result.append(cur_comb[:])
            return
        if cur_sum>target:
            return
        
        for i in range(start_index,len(candidates)):
            if i>start_index and candidates[i]==candidates[i-1]:
                continue
            cur_comb.append(candidates[i])
            backtrack(i+1,cur_comb,cur_sum+candidates[i])
            cur_comb.pop()
       backtrack(0,[],0)
       return result
        