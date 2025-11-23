class Solution:
    def Find_content_children(self, g, s):
        right = left = 0

        count = 0

        while right < len(s) and left < len(g):
            if s[right] >= g[left]:
                count += 1
                left += 1
            else:
                right += 1
        return count

if __name__ == "__main__":
    res = Solution()
    s = [1, 2, 4, 5]
    g = [1, 1, 3, 6]
    print(res.Find_content_children(g, s))
    
