# Elite IIT-Style Array Mastery Program

class ArrayOperations:
    def __init__(self, initial_list=None):
        # Python lists are dynamic arrays under the hood
        self.array = initial_list if initial_list is not None else []

    def reverse_array(self) -> list:
        """Reverses the array in-place using the Two-Pointer technique."""
        # Time Complexity: O(n) | Space Complexity: O(1)
        left, right = 0, len(self.array) - 1
        while left < right:
            self.array[left], self.array[right] = self.array[right], self.array[left]
            left += 1
            right -= 1
        return self.array

    def find_max_subarray_sum(self) -> int:
        """Finds the maximum contiguous subarray sum using Kadane's Algorithm."""
        # Time Complexity: O(n) | Space Complexity: O(1)
        if not self.array:
            return 0
        
        max_so_far = self.array[0]
        current_max = self.array[0]
        
        for num in self.array[1:]:
            current_max = max(num, current_max + num)
            max_so_far = max(max_so_far, current_max)
            
        return max_so_far

    def max_sliding_window_sum(self, k: int) -> int:
        """Finds the maximum sum of any contiguous subarray of size k."""
        # Time Complexity: O(n) | Space Complexity: O(1)
        n = len(self.array)
        if n < k or k <= 0:
            return 0
        
        # Calculate sum of the first window
        window_sum = sum(self.array[:k])
        max_sum = window_sum
        
        # Slide the window across the array
        for i in range(n - k):
            window_sum = window_sum - self.array[i] + self.array[i + k]
            max_sum = max(max_sum, window_sum)
            
        return max_sum

# --- Execution and Testing ---
if __name__ == "__main__":
    # Initialize sample data
    sample_data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    obj = ArrayOperations(sample_data.copy())
    
    print(f"Original Array: {sample_data}")
    
    # 1. Two-Pointer Reverse
    print(f"Reversed Array: {obj.reverse_array()}")
    
    # 2. Kadane's Algorithm (Max Subarray)
    # Reset object with original array
    obj = ArrayOperations(sample_data)
    print(f"Maximum Subarray Sum (Kadane's): {obj.find_max_subarray_sum()}")
    
    # 3. Sliding Window (k = 3)
    # Subarray [4, -1, 2] or [-1, 2, 1] or [2, 1, -5]... Max is [4, -1, 2] -> sum = 5
    print(f"Max Sliding Window Sum (k=3): {obj.max_sliding_window_sum(3)}")
