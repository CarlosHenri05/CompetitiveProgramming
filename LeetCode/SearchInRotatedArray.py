class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left<=right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            
            # Vamos checar se o lado esquerdo está ordenado 
            if nums[left] <= nums[mid]:
                # Se estiver, vamos continuar procurando nesse lado
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    # Se não, procuramos no lado direito
                    left = mid + 1
                
            # Se o lado esquerdo não estiver ordenado, vai cair no else
            else:
                # Continua a procura no lado direito
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                # Se não estiver no lado direito, procuramos no lado esquerdo 
                else:
                    right = mid - 1
            
        return -1

        