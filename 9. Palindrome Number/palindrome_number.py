class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        str_x = str(x)

        if str_x == str_x[::-1]:
            return True
        else:
            return False