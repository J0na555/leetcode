class Solution:
    def sortColors(self, nums):
        nums.sort()
        return nums


if __name__ == "__main__":
    res = Solution()
    arr = [1, 2, 0, 1, 2, 1, 0]
    print(res.sortColors(arr))
