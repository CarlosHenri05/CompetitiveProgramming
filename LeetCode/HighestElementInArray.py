def highestElement(nums):
  high = nums[0]

  for i in range(len(nums)):
    if high<nums[i]:
      high = nums[i]

  return high

nums = [8,10,5,7,9]

print(highestElement(nums))
