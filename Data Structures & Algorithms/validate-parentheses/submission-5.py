class Solution:
    def isValid(self, s: str) -> bool:
        
        # quick escape for odd length strings
        if len(s)%2 == 1:
            return False

        # define the empty stack ds
        stack = []

        # iterate through all character in s
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        
        for c in s:
            if c in opening: # c is an OPENING
                stack.append(c)
            else: # c must be a CLOSING
                if len(stack) > 0:
                    index = opening.index(stack[-1])
                    if closing[index] == c:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
           
        