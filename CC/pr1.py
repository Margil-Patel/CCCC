class MinStack:
    def __init__(self,capacity):
        self.stack = []
        self.capacity = capacity
        self.min_stack = []
    
    def isFull(self):
        return len(self.stack) == self.capacity
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self,value):
        if self.isFull():
            print("Overflow")
            return
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
    
    def pop(self):
        if self.isEmpty():
            print("Empty")
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        return popped
    
    def get_min(self):
        return self.min_stack[-1]
    


capacity = int(input("Enter the size of stack: "))
stack = MinStack(capacity)

for i in range(capacity):
    stack.push(int(input("Enter the values")))

print(stack.pop())
print(stack.get_min())
# print(stack.pop)