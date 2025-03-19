def maximumSubArraySum(nums):

  if len(nums)<1:
      return -1
  
  max_sum = nums[0]

  for i in range(len(nums)):
    curr_sum = 0
    for j in range(i, len(nums)):
      curr_sum = curr_sum+nums[j]

      if max_sum<curr_sum:
        max_sum = curr_sum
  
  return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]

print(maximumSubArraySum(nums))
