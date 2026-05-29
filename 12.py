stack = []

text = "PYTHON"

for ch in text:
    stack.append(ch)

reverse = ""

while stack:
    reverse += stack.pop()

print("Reversed String:", reverse)