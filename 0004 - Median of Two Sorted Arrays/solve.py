class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        return((nums1[l//2]+nums1[(l//2)-1])/2 if l%2==0 else nums1[l//2])