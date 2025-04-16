class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        #first check if input was empty then return empty list

        if not digits:
            return []

        #initialize result to store the output
        result = []

        #initialize a hashmap to store the values 
        phoneMap ={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        #define backtracking function

        def backtrack(index, current_combination):

            #check base case: if length of input equals to index then you can join the current availble string to result and return

            if index == len(digits):
                result.append(\\.join(current_combination))
                return
            #extract the values from hashmap we stored in start
            possible_letters = phoneMap[digits[index]]

            #start loop with each letter and start backtrack

            for letter in possible_letters:
                current_combination.append(letter)
                #backtrack
                backtrack(index+1,current_combination)
                #undo that choice
                current_combination.pop()
        backtrack(0,[])
        return result


        