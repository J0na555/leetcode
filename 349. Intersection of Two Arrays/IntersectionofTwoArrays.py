class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        intersection = []
        seen = set()

        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums1[j] == nums2[i]:
                    if nums2[i] not in seen:
                        intersection.append(nums2[i])
                        seen.add(nums2[i])
                    break
        return intersection

            
