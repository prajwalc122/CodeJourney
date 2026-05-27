def find_duplicate(nums: list[int]) -> int:
    seen = {}

    for num in nums:
        if num in seen:
            return num
        
        seen[num] = 1

    return -1

# Test
print(find_duplicate([1, 3, 4, 2, 2]))