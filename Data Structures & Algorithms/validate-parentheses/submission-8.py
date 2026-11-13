class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for bracket in s:
            if len(stack) > 0:
                if bracket == "(" or bracket == "{" or bracket == "[":
                    stack.append(bracket)
                else:
                    if bracket == ")" and stack[-1] == "(":
                        stack.pop()

                    elif bracket == "}" and stack[-1] == "{":
                        stack.pop()
                        
                    elif bracket == "]" and stack[-1] == "[":
                        stack.pop()
                    
                    else:
                        return False
          
            else:
                stack.append(bracket)
            
        if len(stack) == 0:
            return True
        else:
            return False