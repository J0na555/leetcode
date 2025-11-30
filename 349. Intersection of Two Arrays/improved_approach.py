class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    res = Solution()
    nums2=[1, 3, 4, 2, 5]
    nums1=[2, 4, 5, 7]

    print(res.intersection(nums2, nums1))

    # time complexity

    # O(m+n)

    #space complexity

    # O(m+n)
    
