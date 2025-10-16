class Solution:
    def longestOnes(self, nums, k):
        max_w = 0
        max_zeros = 0
        n = len(nums)
        left = 0

        for right in range(n):
            if nums[right] == 0:
                max_z += 1
            
            while max_z > k:
                if nums[left] == 0:
                    max_zeros -= 1
                left += 1
            
            w = right - left + 1
            max_w  = max(max_w, w)
        
        return max_w
