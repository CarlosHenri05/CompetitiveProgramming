class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)

        # Criamos esses elementos left e right para eles armazenaram o produto dos elementos da esquerda e da direita

        left = 1
        for i in range(len(nums)):
            answer[i] *= left
            left *= nums[i]
        
        right = 1
        # Vai ler do penúltimo elemento (por que teoricamente o right é o ultimo)
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        
        return answer