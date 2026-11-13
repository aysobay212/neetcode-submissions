class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for bracket in s:
            if len(stack) > 0:
                if bracket == "(" or bracket == "{" or bracket == "[":
                    stack.append(bracket)
                else:
                    flag = False
                    if bracket == ")" and stack[-1] == "(":
                        stack.pop()
                        flag = True

                    elif bracket == "}" and stack[-1] == "{":
                        stack.pop()
                        flag = True
                        
                    elif bracket == "]" and stack[-1] == "[":
                        stack.pop()
                        flag = True
                    
                    if not flag:
                        return False
          
            else:
                stack.append(bracket)
            
        if len(stack) == 0:
            return True
        else:
            return False