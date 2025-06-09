class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr = nums1 + nums2

        arr.sort()

        total = len(arr)

        if total % 2 == 1:
            return float(arr[total//2])
        

        return (float(arr[total//2 - 1]) + float(arr[total//2])) / 2
