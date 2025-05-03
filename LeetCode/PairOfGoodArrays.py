class Solution(object):
    def numIdenticalPairs(self, nums):
        hashMap = {}

        count = 0

        for num in nums:
            if num in hashMap:
                counter = hashMap[num]





