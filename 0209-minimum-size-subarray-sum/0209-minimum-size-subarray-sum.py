class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = i_sum = 0
        min_win = float('inf')

        while right < len(nums):
            i_sum += nums[right]

            while i_sum >= target:
                min_win = min(min_win, right - left + 1)
                i_sum -= nums[left]
                left += 1

            right += 1
            
        return min_win if min_win != float('inf') else 0