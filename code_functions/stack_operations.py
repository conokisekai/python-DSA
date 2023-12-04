def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
    
    return not stack

# Testing the function
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
