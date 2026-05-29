class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return "Stack Underflow"
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return "Stack Empty"
        return self.stack[-1]

    def display(self):
        return self.stack


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack:", s.display())

print("Pop:", s.pop())

print("Top:", s.peek())