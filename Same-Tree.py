# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
       #first write the base condition that when it reaches the null it checks for both the tree condition whether both have null or not 
       if not p or not q:
        return p==q
       #now return the conditions we check at every node tp say that it was same tree
       return (p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        