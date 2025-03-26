# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #first lets solve this using DFS recursive method 
        # if not root:
        #     return 0
        # return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

        #second method is we can solve this using dfs iterative method

        # if not root:
        #     return 0
        # stack = [[root,1]]
        # result = 0
        # while stack:
        #     node, depth = stack.pop()
        #     result = max(result,depth)
        #     if node.right:
        #         stack.append([node.right,depth+1])
        #     if node.left:
        #         stack.append([node.left,depth+1])
        # return result

        #third method is to use BFS 
        
        queue = deque()
        if root:
            queue.append(root)
        level = 0
        while queue:
            
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return level
            



        
        