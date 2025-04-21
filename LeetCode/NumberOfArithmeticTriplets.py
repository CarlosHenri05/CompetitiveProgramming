# Brute-force solution O(n³)

class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        count = 0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[j] - nums[i] == diff and nums[k]-nums[j] == diff:
                        count+=1
        
        return count

# Best solution using three pointers O(n)

class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        # Three pointers to track left, mid and right 

        count = 0
        left = 0
        right = 2

        # i is the middle pointer 
        for i in range(1, len(nums)):
            
            while nums[i] - nums[left] > diff: # ->  This means nums[i] - nums[left] > diff, so nums[left] is too small, and we move the left pointer forward.
                left+=1
            
            while right<len(nums)-1 and nums[right] - nums[i] < diff: # -> This means nums[right] - nums[i] < diff, so nums[right] is too small, and we move the right pointer forward.
                right+=1
            
            if nums[i] - nums[left] == diff and nums[right] - nums[i] == diff: 
                count+=1

        return count 
            

        