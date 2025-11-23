class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        # the problem 
        # as long as the number is the equal or less than the next number subtract it and put it in the discount array
        # when it is less than the next number just add the original numbers to the discount array and also do the same for the next numbers

        result = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    discount = prices[j]
                    break
            result.append(prices[i] - discount)
        return result
                
