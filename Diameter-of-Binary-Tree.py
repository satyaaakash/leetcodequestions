# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #define a recursive function to calculate the diameter

        def diameter(node,result):
            #basecase: if node is none , rweturn 0
            if node is None:
                return 0

            #recursively calculate the diameter of left and right subtrees
            left = diameter(node.left,result)
            right = diameter(node.right,result)

            #update the maximum diameter encountered so far 
            result[0] = max(result[0],left+right)

            #return the depth of the current node
            return max(left,right)+1

        #initialize a list to hold the maximum diamter encountered
        result = [0] 
        #call the diameter function starting from root
        diameter(root,result)
        return result[0]    