class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # so the problem is merging the second array on the first array
        # the first array can accomodate both arrays if the second array replaces the 0's from the first array

        # to solve we can compare the elements of each array one by one since they are ordered in the firs place 

        # or i could just  merge the arrays and then sort it with .sort() LoL

        for i in range(n):
            nums1[m+i] = nums2[i]

        return nums1.sort()