def findNumbers(nums):
  if len(nums)<=1:
    return -1
  
  return [i for i in range(1, len(nums)) if i not in nums]

nums = [4,3,2,7,8,2,3,1]



def findNumbersWithSet(nums):
  n = len(nums)

  numsSet = set(nums)

  return [i for i in range(1,n+1) if i not in numsSet]
  

print(findNumbersWithSet(nums))
