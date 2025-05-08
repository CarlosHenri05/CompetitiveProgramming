class Solution(object):
    def intersection(self, nums1, nums2):
        setAns = set()

        for i in range(len(nums1)):
            setAns.add(nums1[i])
        
        for j in range(len(nums2)):
            setAns.add(nums2[j])

        ans = []
        for i in setAns:
            if i in nums1 and i in nums2:
                ans.append(i)
        
        return ans
