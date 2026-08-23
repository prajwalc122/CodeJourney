n = int(input())
arr = list(map(int, input().split()))

# Remove duplicates
unique_arr = list(set(arr))

# Sort in descending order
unique_arr.sort(reverse=True)

# Print second largest
print(unique_arr[1])
