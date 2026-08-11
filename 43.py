arr = [1, 2, 3, 2, 1]

left = 0
right = len(arr) - 1

while left < right:
    if arr[left] != arr[right]:
        print("Not palindrome")
        break

    left += 1
    right -= 1
else:
    print("Palindrome")
