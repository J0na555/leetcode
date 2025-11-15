class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # initiate an empty array
        # iterate over the arra and check if there are numbers that are less that the cuurent number
        # after getting the number add it to the array that was initated
        # do that for all of the numbers and return the array

        smaller_nums = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]
                    count += 1
            smaller_nums.append(count)
        return smaller_nums


