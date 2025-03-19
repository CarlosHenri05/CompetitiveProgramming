
def twoSum(nums, target):
    left = 0
    right = len(nums)-1

    while left<right:
        sum = nums[left]+nums[right]

        if sum == target:
            return [left+1, right+1]
        elif sum>target:
             right-=1
        else:
            left+=1
            
        
            



nums = [2,7,11,15]
target = 9

print(twoSum(nums,target))
        