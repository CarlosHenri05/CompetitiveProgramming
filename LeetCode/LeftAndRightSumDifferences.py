# Preffix and Suffix sum 

class Solution(object):
    def leftRightDifference(self, nums):
        prefix = 0 
        suffix = sum(nums)

        ans = []

        for num in nums:
            prefix += num
            ans.append (abs(prefix-suffix))
            suffix-=num
        
        return ans 
