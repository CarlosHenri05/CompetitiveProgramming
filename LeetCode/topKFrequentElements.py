def sortColors(nums):
    left = 0
    mid = 0
    right = len(nums)-1

    while left<right:
        if nums[mid]==0:
            temp = nums[left]
            nums[left] = nums[mid]
            nums[mid] = temp
            left+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        elif nums[mid]==2:
            temp = nums[right]
            nums[right] = nums[mid]
            nums[mid] = temp
            right-=1


nums = [2,0,2,1,1,0]

sortColors(nums)

print(nums)
