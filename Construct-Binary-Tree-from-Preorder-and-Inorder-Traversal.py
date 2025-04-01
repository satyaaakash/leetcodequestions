# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #if preorder or inorder is empty we return none that is the base condition for this question

        if not preorder or not inorder:
            return None

        #other than this , first we should create root node for tree with preorder first element

        root = TreeNode(preorder[0])

        #now we should assign mid as from inorder , we can saythat before mid was left subtree and after mid was right subtree
        mid = inorder.index(preorder[0])

        #define root.left for building left subtree
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])

        #same way define root.right

        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])

        #finally return root 
        return root
        