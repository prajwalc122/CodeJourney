def count_frequency(nums: list[int]) -> dict:
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq

# Test
print(count_frequency([1, 2, 2, 3, 3, 3]))