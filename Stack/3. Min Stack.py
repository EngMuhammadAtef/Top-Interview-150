class MinStack:
    def __init__(self):
        self.st = []
        self.min=None

    def push(self, val: int) -> None:
        if len(self.st)==0:
            self.st.append(val)
            self.min=val
        else:
            if val>=self.min:
                self.st.append(val)
            else:
                self.st.append(2*val-self.min)
                self.min=val
                
    def pop(self) -> None:
        x=self.st.pop() 
        if x<self.min:
            self.min=2*self.min-x
    
    def top(self) -> int:
        x=self.st[-1]
        if x>=self.min:
            return x
        return self.min

    def getMin(self) -> int:
        return self.min
            
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()