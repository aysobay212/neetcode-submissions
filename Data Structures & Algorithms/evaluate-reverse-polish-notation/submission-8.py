class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for token in tokens:
            try: 
                int(token)
                stack.append(token)
            except ValueError:
                # must be an operator
                v2 = stack.pop()
                v1 = stack.pop()
                expression = f"{v1} {token} {v2}"
                print(expression)
                stack.append(int(eval(expression)))
        print(stack)
        return int(stack[0])
            