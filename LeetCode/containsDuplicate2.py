

def containsNearbyDuplicate( nums, k):
  indexMap = {}

  for index, value in enumerate(nums):
    if value in indexMap and index - indexMap[index] <=k:
      return True
    indexMap[value] =  index 
  return False


nums = [1,2,3,1]
k = 3

print(containsNearbyDuplicate(nums,k))
