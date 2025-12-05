class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack: 
                    stack.pop()
            return stack
        
        return build_string(s) == build_string(t)

if __name__ == "__main__":
    res = Solution()
    s = "ac#d"
    t = "aa#d"
    z = "a#d#"
    x = "c#v"
    print(res.backspaceCompare(s, t))
    print(res.backspaceCompare(z, x))
