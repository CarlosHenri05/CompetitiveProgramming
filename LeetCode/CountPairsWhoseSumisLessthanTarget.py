# Brute-force solution O(n²)
class Solution(object):
    def countPairs(self, nums, target):
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum<target:
                    count+=1
        return count

#Best solution
class Solution(object):
    def countPairs(self, nums, target):
        count = 0
        nums.sort()
        left = 0
        right = len(nums)-1

        while left<right:
            sum = nums[left]+nums[right]
            if sum<target:
                count += right-left
                left+=1
            else:
                right-=1
        
        return count
        

        