text = "PYTHON"

print("Original string:", text)

# 1. Basic slicing
print("First 3 characters:", text[0:3])

# 2. From index to end
print("From index 2:", text[2:])

# 3. From beginning to index
print("First 4 characters:", text[:4])

# 4. Negative slicing
print("Last 3 characters:", text[-3:])

# 5. Remove last 2 characters
print("Without last 2 characters:", text[:-2])

# 6. Every 2nd character
print("Every 2nd character:", text[::2])

# 7. Every 2nd character starting from index 1
print("Every 2nd from index 1:", text[1::2])

# 8. Reverse the string
print("Reversed:", text[::-1])

# 9. Reverse a specific part
print("Reverse part:", text[5:2:-1])

# 10. Negative index slicing
print("Negative slicing:", text[-4:-1])
