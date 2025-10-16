class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        left , right = 0, 0 
        result = set()

        for right in range(len(nums)):
            if right - left > k:
                result.remove(nums[left])
                left += 1
            if nums[right] in result:
                return True
            result.add(nums[right])
        return False
        