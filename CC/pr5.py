def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack, result = [], ""
    
    for char in expression:
        if char.isalnum():
            result += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            while stack and precedence.get(stack[-1], 0) >= precedence[char]:
                result += stack.pop()
            stack.append(char)
    
    while stack:
        result += stack.pop()
    
    return result