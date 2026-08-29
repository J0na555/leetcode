class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort the element first
        # then try to count the element that are the same increament the count 
        # at end make sure to keep track of the highest one
        #-----------------
        # use boyer moore algorithm


        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

