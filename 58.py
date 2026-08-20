def array_sum(arr, n):
    if n == 0:
        return 0
    return arr[n-1] + array_sum(arr, n-1)

arr = [1, 2, 3, 4]
print(array_sum(arr, len(arr)))  # 10
