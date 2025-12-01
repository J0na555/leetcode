class Solution(object):
    def findMaxAverage(self, nums, k):
        s = sum(nums[:k])   
        m = s              
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]  
            if s > m:
                m = s
        return m / float(k)


if __name__ == "__main__":
    res = Solution()
    arr =  [1,12,-5,-6,50,3]
    k = 4
    print(res.findMaxAverage(arr, k))
