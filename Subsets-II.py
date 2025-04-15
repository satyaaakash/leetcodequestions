class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start_index,subset):
            result.append(subset[:])

            for i in range(start_index,len(nums)):
                if i>start_index and nums[i]==nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i+1,subset)
                subset.pop()
        backtrack(0,[])
        return result
        