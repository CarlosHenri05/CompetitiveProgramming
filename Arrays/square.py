import math


def sortedSquares( nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    nums.sort()

    return nums

nums = [5,3,2,1,4]
print(sortedSquares( nums ))
    
        