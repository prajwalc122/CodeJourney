stack = [10,110,111]
'''
# Push operation
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)
'''
# Pop operation
removed = stack.pop()
print("Popped element:", removed)

print("Stack after pop:", stack)

# Peek (top element)
print("Top element:", stack[-1])