# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # #two methods to solve this question
        # #method one is two use two functions one is same tree function and other is to check, traverse each node in main tree and when both nodes are equal you call that fucntion.

        # #method 1
        # def isSameTree(p,q):
        #     #check if one of them is null then check if both are equal or not , this would be the base condition for this question
            
        #     if not p or not q:
        #         return p==q
        #     return p.val==q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        
        # def helper(root,subRoot):
        #     if not root:
        #         return False
        #     #here it checks for the main condition, i.e whether the the node values are equal and also their tree are same, if yes then return true
        #     if root.val == subRoot.val and isSameTree(root,subRoot):
        #         return True
        #     #if not then they will check for main trre root.left or root.right with sub tree and return
        #     return helper(root.left,subRoot) or helper(root.right,subRoot)
        
        # #in main function at start will call helper function to start the process
        # return helper(root,subRoot)


        #method2 - serialiazation
        def serialize(root):
            if not root:
                return \N\
            return f\({root.val},{serialize(root.left)},{serialize(root.right)})\
        rootSerialized = serialize(root)
        subRootSerialized = serialize(subRoot)

        return subRootSerialized in rootSerialized

            