def two_sum(nums: list[int], target: int) -> list[int]:
    # Stores seen numbers and their indices: {number: index}
    seen = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement is already in our hash map
        if complement in seen:
            return [seen[complement], index]
            
        # Otherwise, store the current number and index
        seen[num] = index
        
    return []  # Return empty list if no solution exists

# Test
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
