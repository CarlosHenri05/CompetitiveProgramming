# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Não é a melhor solução, depois vou tentar melhorar pensando nos fundamentos de uma BST.
# 52 ms Beats 20.50% -> Runtime 
# 28.83 MB Beats 32.75% -> Memory

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        self.sum = 0
        def dfs(node, low, high):
            if not node:
                return 0 
            
            if node.val >= low and node.val<=high:
                self.sum+=node.val
            
            dfs(node.left, low, high)
            dfs(node.right, low, high)
        
        dfs(root, low, high)

        return self.sum
        