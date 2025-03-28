class Solution(object):
    def getSneakyNumbers(self, nums):
        count = Counter(nums)
        arr = set()

        for i in range(len(nums)):
            if count[nums[i]]>=2:
                arr.add(nums[i])

        arr = list(arr)
                
        return arr
