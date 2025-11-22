class Solution:
    def removeElement(self, nums, val):
        # iterate over the list and if there is an element that is equeal to the value then remove that number from the array
        left = 0
        right = len(nums)

        while left < right:
            if nums[left] == val:
                nums[left] == nums[right - 1]
                right -= 1
            else:
                left += 1
        return right



if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 4, 1, 3, 2]
    val = 2

    print(s.removeElement(nums, val))


