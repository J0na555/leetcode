class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = Counter(s)

        sorted_chars = sorted(s, key=lambda x: (-freq[x], x))
        
        return ''.join(sorted_chars)
