# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        ans = []

        def bfs(node, arr, level):
            if not node:
                return 
            
            if len(arr)<=level:
                arr.append([])
            
            arr[level].append(node.val)

            bfs(node.left, arr, level + 1)
            bfs(node.right, arr, level + 1)
        
        bfs(root, ans, 0)

        return ans


        
        

        