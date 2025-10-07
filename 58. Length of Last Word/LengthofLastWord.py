class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        splitted_word = s.split()
        last_string = splitted_word[-1]

        return len(last_string)