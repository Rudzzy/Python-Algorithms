# The array increases then decreases – find the peak index.

def peakIndexInMountainArray(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

print(peakIndexInMountainArray([0, 2, 4, 7, 5, 3, 1]))  # 3
print(peakIndexInMountainArray([0, 10, 5, 2]))          # 1
