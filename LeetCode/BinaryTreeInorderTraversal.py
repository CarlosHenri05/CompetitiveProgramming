# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        self.recursive_inorder(root, result)
        return result
    
    def recursive_inorder(self, node, result):
        if node:
            self.recursive_inorder(node.left, result)
            result.append(node.val)
            self.recursive_inorder(node.right,result)

        