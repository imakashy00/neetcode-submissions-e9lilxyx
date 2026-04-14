class MinStack:

    def __init__(self):
        self.stack:list[int] = []
        self.stack_min:int = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.stack_min = val
        else:
            self.stack.append(val-self.stack_min)
            self.stack_min = min(val,self.stack_min)

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop < 0 :
            self.stack_min = self.stack_min - pop
        
    def top(self) -> int:
        top = self.stack[-1]
        if top < 0:
            return self.stack_min
        else:
            return self.stack_min + top        

    def getMin(self) -> int:
        return self.stack_min
        
