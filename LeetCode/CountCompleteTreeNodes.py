class Solution(object):
    def countNodes(self, root):
        nums = []

        def dfs(root, nums):
            if root:
                dfs(root.left, nums)

                nums.append(root.val)

                dfs(root.right, nums)
        
        dfs(root, nums)
        
        return len(nums)
    
  # Sinto que poderiamos resolver sem a memória adicional da array, vou tentar aplicar a resolução abaixo 

class Solution(object):
  def countNodes(self, root):
      if not root:
        return 0
      
      return 1 + self.countNodes(root.left) + self.countNodes(root.right)
