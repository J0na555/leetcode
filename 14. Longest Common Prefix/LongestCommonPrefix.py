class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        
        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                 # if the word is equal to the length of the list(the last element of base is len(strs)) or the words are not matching
                if (i == len(word) or word[i] != base[i]):
                    return base[0:i] 
        return base

# vertical scanning like...make the first word as a base then compare it vertically to the other words


