class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()        
        res = ''

        for char in s:
            if char.isalnum():                
                res += char
        
        return res == res[::-1]