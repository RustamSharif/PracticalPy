class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)

def is_balanced_brackets(s):
    stack = Stack()
    brackets_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in brackets_map.values():  # If it's an opening bracket, push to stack
            stack.push(char)
        elif char in brackets_map:  # If it's a closing bracket, check conditions
            if stack.is_empty() or stack.peek() != brackets_map[char]:
                return "Несбалансированно"
            stack.pop()
    
    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"

# Example usage
print(is_balanced_brackets("(((([{}]))))"))
print(is_balanced_brackets("{{[(])]}}"))