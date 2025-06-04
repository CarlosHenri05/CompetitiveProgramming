class Solution(object):
    def missingNumber(self, nums):
        x = 0
        n = len(nums)

        for num in nums:
            x ^= num

        for i in range(n+1):
            x^=i
        
        return x
            
        