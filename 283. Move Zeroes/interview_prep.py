class Solution:
    def moveZeroes(self, nums):
        # the problem 
        # we declare two pointers one at the beginning and one at the end of the array
        # the first pointer moves unitl it get's to zero 
        # while the second pointer waits on the last index 
        # when the first pointer gets to zero they both swap positions and we decrement one from the second pointer 
 

        left, right = 0, len(nums) - 1

        for left in range(len(nums)-1):
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        return nums

if __name__ == "__main__":
    res = Solution()
    nums = [0, 1, 0, 3, 12, 3, 0, 3, 4, 5, 6]
    print(nums)
    print(res.moveZeroes(nums))




