class Solution(object):
    def numIdenticalPairs(self, nums):
        hashMap = {}

        count = 0

        for num in nums:
            if num in hashMap:
                count += hashMap[num]
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        return count # tempo = O(n) e space = O(1)

        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count+=1
        
        # return count

        # # 1,2,3,1,1,3 O(n²)
