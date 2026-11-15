class MinStack:

    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.aux.append(val)
        else:
            if self.aux[-1] > val:
                self.aux.append(val)
            else:
                self.aux.append(self.aux[-1])
        self.stack.append(val)
        return
        

    def pop(self) -> None:
        # called on non-empty stacks
        self.stack.pop()
        self.aux.pop()
        return
        

    def top(self) -> int:
        # called on non-empty stacks
        return self.stack[-1]
        

    def getMin(self) -> int:
        # called on non-empty stacks
        return self.aux[-1]
        
