def twoSum(nums, target):
  sumMap = {}
  for i in range(len(nums)):
    diferenca = target-nums[i]
    if diferenca in sumMap:
      return {sumMap[diferenca], i}
    else:
      sumMap.update({nums[i]:i})
  
  return -1

nums = [2,7,11,15]
alvo = 9

print(twoSum(nums,alvo))
