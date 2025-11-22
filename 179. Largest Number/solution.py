class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        str_nums = list(map(str, nums))
        n = len(str_nums)
        
        for i in range(n):
            for j in range(0, n-i-1):
                if str_nums[j] + str_nums[j+1] < str_nums[j+1] + str_nums[j]:
                    str_nums[j], str_nums[j+1] = str_nums[j+1], str_nums[j]
        
        result = ''.join(str_nums)
        return '0' if result[0] == '0' else result

        


        # the first method
        # sort the numbers by shuffling the list by one and seeing if that's the largest number that i got since
        # the first methond dont work
        # second method 
        # make a custom bubble sort and sort it based on that
