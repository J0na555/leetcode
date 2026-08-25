class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
       # we use two piinters one at the start and one at the end
       # we check if the first pointer points to val if exchange it with the val of the last pointer 

        left, right = 0, len(nums)-1

        while left <= right:
            if nums [left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                del nums[right+1]
            else:
                left += 1
        