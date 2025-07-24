# Problem: Find the minimum element in a rotated sorted array with no duplicates.

def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

print(findMin([3, 4, 5, 1, 2]))  # 1
print(findMin([11, 13, 15, 17]))  # 11
print(findMin([2, 1]))  # 1