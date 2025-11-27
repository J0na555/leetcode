# there are no arrays that have numbers that is less than 2
# what happened if the numbers dont add up to the target


# approach 
# check if there are numbers in the array that add up to the target with for loop 
# if there are break and return the indexes of the two numbers
# if there are no numbers that add up to the target with the first number then check the second number and go with out checking the previos number 
# if there are no numbers that add up to the target then return 0

class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


if __name__ == '__main__':
    res = Solution()
    nums1 = [3, 2, 4]
    nums2 = [3, 3]
    nums3 = [2, 7, 11, 15]

    print(res.twoSum(nums1, 6))
    print(res.twoSum(nums2, 6))
    print(res.twoSum(nums3, 9))


