# thought process
# there are three things we must keep in mind
    # 1.Open brackets must be closed by the same type of brackets.
    # 2.Open brackets must be closed in the correct order
    # 3.Everyclose bracket has a corresponding open bracket of the same type.
# i can dict and make the keys the closing brackets and make the keys the opening brackets
# then make a stack and 
# if the current bracket is an opening one then append it 
# if it's a closing bracket pop the last one and check if it matched with the closing bracket
    # if it does match then continue
    # if not then break and return false

class Solution:
    def validParenthesis(self, stack):
        brackets = { ')': '(', '}': '{', ']': '[' }

        sym_stack = []

        for sym in stack:
            if 




