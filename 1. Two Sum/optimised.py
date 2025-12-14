class Solution(object):
    def twoSum(self, nums: list[int], target: int):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

if __name__ == '__main__':
    res = Solution()
    nums1 = [3, 2, 4]
    nums2 = [3, 3]
    nums3 = [2, 7, 11, 15]

    print(res.twoSum(nums1, 6))
    print(res.twoSum(nums2, 6))
    print(res.twoSum(nums3, 9))

    # time complexity 0(n)
    # space complexity 0(n)
