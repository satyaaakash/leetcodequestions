# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        \\\Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        \\\
        
        result =[]
        def preorder(root):
            if not root:
                result.append('N')
                return

            result.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(result)

    def deserialize(self, data):
        \\\Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        \\\
        nodevalues = data.split(',')
        self.i = 0

        def construct():
            nodevalue = nodevalues[self.i]
            self.i+=1
            if nodevalue == \N\:
                return None
            node = TreeNode(int(nodevalue))
            node.left = construct()
            node.right = construct()
            return node
        return construct()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))