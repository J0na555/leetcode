# return the numbers that are present in both arrays in an arrays

# iterate on the first array with the second array and cross check if there are any simillar numbers
# for num1[i] we search num2[j] that's equal with that number if there are we return as an array 


class Solution:
    def intersection(self, nums1, nums2):

        intersection = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if nums1 not in intersection:
                        intersection.append(nums1[i])
        return intersection

if __name__ == "__main__":
    res = Solution()
    nums1 = [1, 2, 3, 5, 1]
    nums2 = [2, 3, 6, 7, 8]
    print(res.intersection(nums1, nums2))


 # time ccmplexity = O(m*n*k) 
# m- len of num1, n len of num2, k len of intersection result
 # space complexity =  O(k)
# -------------------
