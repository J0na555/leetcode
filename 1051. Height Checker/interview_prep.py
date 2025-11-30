class Solution:
    def heightChecker(self, height):
        j=1
        for i in range(len(height)):
            if height[j] >= height[i]:
                j+=1
            return j-1
        return j-1

if __name__ == "__main__":
    height=[1, 3, 5, 4, 6]
    res = Solution()
    print(res.heightChecker(height))

    
