# the problem

# the numbers are unique
# in the array that is given there is one number that is missing
# count = max(nums)
# my approach
# i am gonna save the len of the array and i am gonna go until the count number and then if there are any nums that are not present return them 

class Solution:
    def missingNumber(self, nums):
       
        num_set = set(nums)
        for i in range(len(nums)):
            if i not in num_set:
                return i
        return 0


if __name__ == "__main__":
    res = Solution()

    print(res.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1 ]))

