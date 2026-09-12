# 1. Reverse Array
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
    return arr


# 2. Largest Element
def largest(arr):
    max_val = arr[0]
    
    for num in arr:
        if num > max_val:
            max_val = num
            
    return max_val


# 3. Second Largest Element
def second_largest(arr):
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second


# 4. Move Zeros to End
def move_zeros(arr):
    j = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
            
    return arr


# 5. Check if Array is Sorted
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# 6. Two Sum
def two_sum(arr, target):
    seen = {}
    
    for i in range(len(arr)):
        diff = target - arr[i]
        
        if diff in seen:
            return [seen[diff], i]
        
        seen[arr[i]] = i
        
    return []


# ------------------ TESTING ------------------

arr = [1, 2, 3, 4, 5]
print("Reverse:", reverse_array(arr.copy()))

print("Largest:", largest([10, 5, 20, 8]))

print("Second Largest:", second_largest([10, 20, 4, 45, 99]))

print("Move Zeros:", move_zeros([0, 1, 0, 3, 12]))

print("Is Sorted:", is_sorted([1, 2, 3, 4]))

print("Two Sum:", two_sum([2, 7, 11, 15], 9))
