n = 5

operations = [
    [1, 2, 100],
    [2, 5, 200],
    [3, 4, 100]
]

arr = [0] * n

for a, b, k in operations:
    for i in range(a - 1, b):
        arr[i] += k

print(arr)
print("Maximum:", max(arr))
