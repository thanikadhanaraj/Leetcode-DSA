class Solution:
    def merge(self, nums1, m, nums2, n):
        l = nums1[:m] + nums2
        l.sort()
        nums1[:] = l