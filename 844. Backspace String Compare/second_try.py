class Solution:
    def backspaceString(self, s, t):
    # make a def
    # build a stack 
    # if the element is alphabet append it to the stack
    # if the element is not an alphabet then pop the last element
    # return the stack 
    # this is the whole def then we just compare both the strings with the def and return true or false

        def backspace(string):
            stack = []
            for char in string:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack
        return backspace(s) == backspace(t) 

if __name__ == "__main__":
    res = Solution()
    str1 = "a#v#"
    str2 = "sv##"
    str3 = "sv#"
    str4 = "sfr"
    print(res.backspaceString(str1, str2))
    print(res.backspaceString(str3, str4))
