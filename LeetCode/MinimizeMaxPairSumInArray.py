class Solution(object):
    def minPairSum(self, nums):
        nums.sort()

        left = 0
        right = len(nums)-1

        max_sum = 0

        while left<right:
            current_sum = nums[left]+nums[right]

            max_sum = max(max_sum, current_sum)

            left+=1
            right-=1
        
        return max_sum 

        # 2,3,3,5

        # 2+5 = 7

        # 3+3 = 6

        # (7,6) -> retorna o maior daqui 
