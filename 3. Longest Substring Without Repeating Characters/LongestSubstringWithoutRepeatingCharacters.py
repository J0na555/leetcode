class Solution(object):
    def lengthOfLongestSubstring(self, s):

        result = 0
        for i in range(len(s)):
            seen = []
            for j in range(i, len(s)):
                
                if s[j] in seen:
                    break
                seen.append(s[j])
                result = max(result, len(seen))
        return result
       
















