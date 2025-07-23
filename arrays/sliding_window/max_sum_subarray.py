def max_sum_subarray(arr, k):
    max_sum = 0
    window_sum = 0
    left = 0

    for right in range(len(arr)):
        window_sum += arr[right]
        if right >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[left]
            left += 1

    return max_sum

# Test cases
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9 (5+1+3)
print(max_sum_subarray([1, 2, 3, 4, 5], 2))     # Output: 9 (4+5)
print(max_sum_subarray([5], 1))                # Output: 5
