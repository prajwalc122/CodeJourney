def count_occurrence(arr, x):
    count = 0                   # Counter
    for num in arr:             # Traverse array
        if num == x:            # Match found
            count += 1
    return count
