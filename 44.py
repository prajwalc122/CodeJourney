arr = [1, 2, 3, 2, 1]

left = 0
right = len(arr) - 1

is_palindrome = True

while left < right:

    if arr[left] != arr[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")
