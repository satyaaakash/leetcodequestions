class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result =[]

        def backtrack(start_index, current_comb, current_sum):
            if current_sum == target:
                result.append(current_comb[:])
                return
            if current_sum>target:
                return
            
            for i in range(start_index,len(candidates)):
                if i>start_index and candidates[i]==candidates[i-1]:
                    continue
                current_comb.append(candidates[i])
                backtrack(i+1,current_comb,current_sum+candidates[i])
                current_comb.pop()
        backtrack(0,[],0)
        return result
        