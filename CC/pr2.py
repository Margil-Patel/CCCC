class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")
    
    def is_empty(self):
        return len(self.stack) == 0

def evaluate_postfix(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}
    tokens = expression.split()
    
    for token in tokens:
        if token not in operators:
            stack.push(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            stack.push(result)
    
    return stack.pop()

# Example usage
if __name__ == "__main__":
    expression = "2 3 + 5 *"
    result = evaluate_postfix(expression)
    print(f"Result of '{expression}' is: {result}")
    
    expression = "10 2 8 * + 3 -"
    result = evaluate_postfix(expression)
    print(f"Result of '{expression}' is: {result}")
