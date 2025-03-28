# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node: #when you reach leaf node it will return 0 which is base case
                return 0
            left = check(node.left) #check left side of every node if it is -1 then tree is unbalanced
            if left ==-1:
                return -1
            right = check(node.right) #same way checks for right side 
            if right ==-1:
                return -1
            if abs(left-right)>1: #even if the difference of heights(left and right) is >1 , which is main condition to check it is balanced or not.
                return -1
            return max(left,right)+1 #if none of the cases executed above then we check the height of the tree and returns it 
        return check(root)!=-1 #in main function we call the defined function to check whether tree was balanced or not if it doesnot return -1 then answer will be true.
        