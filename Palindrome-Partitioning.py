class Solution:
    def partition(self, s: str) -> List[List[str]]:

        #initialize a result list to return the output
        result =[]

        #define a backtrack function 

        def backtrack(start_index,current_partition):

            #base case 1: check the length of startindex and string length was equal then you can append that partition into result 

            if start_index ==len(s):
                result.append(current_partition[:])
                return
            
            #start for loop for recursive backtracking 

            for end_index in range(start_index, len(s)):

                #find substring through slicing to extract and pass that to check whether it is palindrome or not
                substring = s[start_index:end_index+1]

                if self.is_palindrome(substring):

                    #now append that to current_partition
                    current_partition.append(substring)
                    #call backtrack for next character
                    backtrack(end_index+1,current_partition)
                    #undo that choice so pop
                    current_partition.pop()
        #call initial backtrack with 0
        backtrack(0,[])
        return result
    #define is palindrome
    def is_palindrome(self,substring):
        return (substring==substring[::-1])
