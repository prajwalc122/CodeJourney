arr = [1, 2, 3, 4, 6]
target = 6

l, r = 0, len(arr)-1

while l < r:
    s = arr[l] + arr[r]
    if s == target:
        print("Found")
        break
    elif s < target:
        l += 1
    else:
        r -= 1
