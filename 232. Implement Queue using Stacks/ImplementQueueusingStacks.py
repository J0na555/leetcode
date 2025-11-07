class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
    def pop(self) -> int:
        while self.stack1:
            return self.stack1.pop()
        return None

    def peek(self) -> int:
        while self.stack1:
            return self.stack1[-1]
        return None

    def empty(self) -> bool:
        while self.stack1:
            return False
        return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
