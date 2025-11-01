class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        
        max_vote = 0

        majority_element = None

        for num, freq in count.items():

            if freq > max_vote:

                max_vote = freq
                majority_element = num

        return majority_element
