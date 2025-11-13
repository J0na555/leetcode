class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # sort
        # compare
        sorted_height = sorted(heights)
        diff = 0

        for i in range(len(sorted_height)):
            if heights[i] != sorted_height[i]:
                diff +=1
        return diff
