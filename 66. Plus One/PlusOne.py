class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for num in digits:
            add_one = int("".join(map(str, digits)))

            add_one += 1

        add_one_arr = [int(digit) for digit in str(add_one)]

        return add_one_arr