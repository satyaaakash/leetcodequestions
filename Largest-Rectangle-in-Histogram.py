class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #initialize both maxarea and stack to be zero
        maximum_area = 0
        stack = []
        #run loop with index and height through heights list
        for i,h in enumerate(heights):
            start = i #assign index value to start , to keep track of index values we can use it update the stack next element
            #if the stack top element height is greater than the current height then will pop the element because it cannot extend further to contribute to maximum_area , so will pop and we will check the maximum area it can bring.
            while stack and stack[-1][1]>h: 
                index,height =stack.pop()
                #area will calculate h* breadth value is like the current index - the top element index 
                maximum_area = max(maximum_area, height *(i-index))
                #update the start to popped stack element index , like to start from there for next element 
                start = index
            #after each i append them to stack
            stack.append((start,h))
        #for remaining elements in stack we need to calculate the maximum area it can contribiute and return the maximum_Area
        for i,h in stack:
            #here to calculate breadth we use total elements -index and find area
            maximum_area = max(maximum_area, h*(len(heights)-i))
        return maximum_area


    #this problem is solved technically with monotonic increasing stack method which ahd time complexity of o(n) and space: o(n)

        