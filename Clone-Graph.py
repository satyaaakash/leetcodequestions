\\\
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
\\\

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node :
            return None
        
        start = node
        old_to_new = {}
        stack = [start]
        visited = set()
        visited.add(start)

        while stack:
            node = stack.pop()
            old_to_new[node] = Node(val=node.val)

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        for old, new in old_to_new.items():
            for neighbor in old.neighbors:
                new_neighbor = old_to_new[neighbor]
                new.neighbors.append(new_neighbor)
        return old_to_new[start]