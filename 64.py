def two_sum(arr, target):
    lookup = {}  # number -> index

    for i, num in enumerate(arr):
        needed = target - num
        
        if needed in lookup:
            return [lookup[needed], i]
        
        lookup[num] = i

    return []  # fallback (problem guarantees one solution)
