def is_sorted(arr):
    for i in range(len(arr)-1):      # Compare adjacent elements
        if arr[i] > arr[i+1]:       # If order breaks
            return False
    return True
