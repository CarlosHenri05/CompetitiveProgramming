from collections import Counter

def numIdenticalPairs(nums):
  for i in range(len(nums)):
    count = 0
    for j in range(i+1, len(nums)):
      if nums[i] == nums[j] and i<j:
        count+=1
  return count


def numIdenticalPairs2(nums):
  goodpairs_count = 0

  occur = Counter(nums)

  for num in nums:
    goodpairs_count+=occur[nums]

    occur[nums]+=1

  return goodpairs_count

print(numIdenticalPairs2([1,2,3,1,1,3]))

