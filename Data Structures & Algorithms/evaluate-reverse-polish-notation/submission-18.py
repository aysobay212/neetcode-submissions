class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        """
        NOTE: use int() as minimally as possible
        """
        if len(tokens) == 1:
            return int(tokens[0])
        
        # we can treak `tokens` as a stack where we pop from left to right the numbers only
        stack = []

        for tok in tokens:

            if tok in ["+", "-", "*", "/"]:
                # find which operand it is
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if tok == "+":
                    stack.append(num1 + num2)
                
                elif tok == "-":
                    stack.append(num1 - num2)
                
                elif tok == "*":
                    stack.append(num1 * num2)
                
                elif tok == "/":
                    stack.append(num1 / num2)
            else:
                stack.append(tok)
        return int(stack[-1])
                
                
        